// -*- C++ -*-
#include "Rivet/Analysis.hh"
#include "Rivet/RivetAIDA.hh"
#include "Rivet/Tools/Logging.hh"
#include "Rivet/Projections/FinalState.hh"
#include "Rivet/Projections/FastJets.hh"
#include "Rivet/Tools/BinnedHistogram.hh"

namespace Rivet {


  class CMS_TEST_ANALYSIS : public Analysis {

  private:
    BinnedHistogram<double> _hist_sigma_AK3;
    BinnedHistogram<double> _hist_sigma_AK5;
    BinnedHistogram<double> _hist_sigma_AK7;

  public:

    /// @name Constructors etc.
    //@{


    /// Constructor
    CMS_TEST_ANALYSIS()
      : Analysis("CMS_TEST_ANALYSIS")
	//,
        //_filter(fastjet::Filter(fastjet::JetDefinition(fastjet::cambridge_algorithm, 0.3), fastjet::SelectorNHardest(3))),
        //_trimmer(fastjet::Filter(fastjet::JetDefinition(fastjet::kt_algorithm, 0.2), fastjet::SelectorPtFractionMin(0.03))),
        //_pruner(fastjet::Pruner(fastjet::cambridge_algorithm, 0.1, 0.5))
    {
      setBeams(PROTON, PROTON);
      setNeedsCrossSection(true);
    }

    //@}


  public:

    /// @name Analysis methods
    //@{

    /// Book histograms and initialise projections before the run
    void init() {
      const FinalState fs;
      //      addProjection(fs, "FS");

      // Jet collections
      addProjection(FastJets(fs, FastJets::ANTIKT, 0.3), "JetsAK3");
      addProjection(FastJets(fs, FastJets::ANTIKT, 0.5), "JetsAK5");
      addProjection(FastJets(fs, FastJets::ANTIKT, 0.7), "JetsAK7");

      //_h_spectra_ak3 = bookHistogram1D(1, 1, 1);
      //_h_spectra_ak5 = bookHistogram1D(2, 1, 1);

      _hist_sigma_AK3.addHistogram(0.0,0.5, bookHistogram1D(1,1,1));
      _hist_sigma_AK3.addHistogram(0.5,1.0, bookHistogram1D(2,1,1));
      _hist_sigma_AK3.addHistogram(1.0,1.5, bookHistogram1D(3,1,1));
      _hist_sigma_AK3.addHistogram(1.5,2.0, bookHistogram1D(4,1,1));

      _hist_sigma_AK5.addHistogram(0.0,0.5, bookHistogram1D(5,1,1));
      _hist_sigma_AK5.addHistogram(0.5,1.0, bookHistogram1D(6,1,1));
      _hist_sigma_AK5.addHistogram(1.0,1.5, bookHistogram1D(7,1,1));
      _hist_sigma_AK5.addHistogram(1.5,2.0, bookHistogram1D(8,1,1));

      _hist_sigma_AK7.addHistogram(0.0,0.5, bookHistogram1D(9,1,1));
      _hist_sigma_AK7.addHistogram(0.5,1.0, bookHistogram1D(10,1,1));
      _hist_sigma_AK7.addHistogram(1.0,1.5, bookHistogram1D(11,1,1));
      _hist_sigma_AK7.addHistogram(1.5,2.0, bookHistogram1D(12,1,1));
      
    }


    // Find the pT histogram bin index for value pt (in GeV), to hack a 2D histogram equivalent
    /// @todo Use a YODA axis/finder alg when available
    //size_t findPtBin(double ptJ) {
    //  const double ptBins_dj[N_PT_BINS_dj+1] = { 220.0, 300.0, 450.0, 500.0, 600.0, 800.0, 1000.0, 1500.0};
    //  for (size_t ibin = 0; ibin < N_PT_BINS_dj; ++ibin) {
    //    if (inRange(ptJ, ptBins_dj[ibin], ptBins_dj[ibin+1])) return ibin;
    //  }
    //  return N_PT_BINS_dj;
    //}


    /// Perform the per-event analysis
    void analyze(const Event& event) {
      const double weight = event.weight();

      const FastJets &fjAK3 = applyProjection<FastJets>(event,"JetsAK3");
      const Jets& jetsAK3 = fjAK3.jets(1*GeV, 1000*GeV, -4.7, 4.7, RAPIDITY);
      
      const FastJets &fjAK5 = applyProjection<FastJets>(event,"JetsAK5");
      const Jets& jetsAK5 = fjAK5.jets(1*GeV, 1000*GeV, -4.7, 4.7, RAPIDITY);
      
      const FastJets &fjAK7 = applyProjection<FastJets>(event,"JetsAK7");
      const Jets& jetsAK7 = fjAK7.jets(1*GeV, 1000*GeV, -4.7, 4.7, RAPIDITY);

      
      //const PseudoJets& psjetsAK3 = applyProjection<FastJets>(event, "JetsAK3").pseudoJetsByPt( 1.0*GeV );
      //const PseudoJets& psjetsAK5 = applyProjection<FastJets>(event, "JetsAK5").pseudoJetsByPt( 1.0*GeV );
      // ... and fill the histograms
      // for(unsigned int a = 0;a<psjetsAK3.size();++a){
      // 	if (abs(psjetsAK3[a].eta()) <= 2)
      // 	  _h_spectra_ak3->fill(psjetsAK3[a].pt(),weight);
      // }
      
      // for(unsigned int a = 0;a<psjetsAK5.size();++a){
      // 	if (abs(psjetsAK5[a].eta()) <= 2)
      // 	  _h_spectra_ak5->fill(psjetsAK5[a].pt(),weight);
      // }
      
      foreach(const Jet &j, jetsAK3){
	_hist_sigma_AK3.fill(fabs(j.momentum().rapidity()), j.momentum().pT(), weight);
      }

      foreach(const Jet &j, jetsAK5){
       	_hist_sigma_AK5.fill(fabs(j.momentum().rapidity()), j.momentum().pT(), weight);
      }

      foreach(const Jet &j, jetsAK7){
      	_hist_sigma_AK7.fill(fabs(j.momentum().rapidity()), j.momentum().pT(), weight);
      }


    }
    
    
    /// Normalise histograms etc., after the run
    void finalize() {
      //const double normalizationVal = crossSection()/sumOfWeights()/2; // the 2 is for absolute eta from -2 to +2
      // normalize(_h_spectra_ak3, normalizationVal);
      // normalize(_h_spectra_ak5, normalizationVal);

      _hist_sigma_AK3.scale(crossSection()/sumOfWeights()/2, this);
      _hist_sigma_AK5.scale(crossSection()/sumOfWeights()/2, this);
      _hist_sigma_AK7.scale(crossSection()/sumOfWeights()/2, this);
      
    }
    
    
  };
  
  
  
  // The hook for the plugin system
  DECLARE_RIVET_PLUGIN(CMS_TEST_ANALYSIS);
  
  
}
