/***
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% P3: Phenomenology of Particle Physics
%%
%% Author:  André Rubbia
%%
%% Section 5.5 Energy-momentum 4-vector
%%
%% This work is licensed under the Creative Commons Attribution 4.0 International License.
%% To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/ or
%% send a letter to Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.
%%
%% PYTHIA is licenced under the GNU GPL v2 or later.
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
**/

// This is a simple test program to illustrate the parton shower in high-energy proton-proton collisions.

#include "Pythia8/Pythia.h"
using namespace Pythia8;

int main() {

  // Generator. Process selection. LHC initialization. Histogram.
  Pythia pythia;
  pythia.readString("Beams:eCM = 13000.");          // set the center-of-mass energy
  pythia.readString("HardQCD:all = on");		    // we want to look at jets
  pythia.readString("PhaseSpace:pTHatMin = 20."); // only those with transverse p > 20 GeV
  pythia.init();

  Hist mult("charged multiplicity", 100, -0.5, 799.5);
  // Begin event loop. Generate event. Skip if error. List first one.
  for (int iEvent = 0; iEvent < 100; ++iEvent) {
    if (!pythia.next()) continue;
    // Find number of all final charged particles and fill histogram.
    int nCharged = 0;
    for (int i = 0; i < pythia.event.size(); ++i)
      if (pythia.event[i].isFinal() && pythia.event[i].isCharged())
        ++nCharged;
    mult.fill( nCharged );
  // End of event loop. Statistics. Histogram. Done.
  }
  pythia.stat();
  cout << mult;
  return 0;
}
