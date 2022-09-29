/***
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% P3: Phenomenology of Particle Physics
%%
%% Author:  André Rubbia
%%
%% Section 19.6 Monte-Carlo Parton Shower
%%
%% This work is licensed under the Creative Commons Attribution 4.0 International License.
%% To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/ or
%% send a letter to Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.
%%
%% PYTHIA is licenced under the GNU GPL v2 or later.
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
**/

// This is a simple test program to illustrate parton shower in e+e- collisions.

#include "Pythia8/Pythia.h"
using namespace Pythia8;

int main() {
  // Generator.
  Pythia pythia;

  // Process selection.
  pythia.readString("Beams:frameType = 2");
  // The type of particle (electron, positron)
  pythia.readString("Beams:idA =  11");
  pythia.readString("Beams:idB = -11");
  // the energy of each beam in GeV
  pythia.settings.parm("Beams:eA", 10.);
  pythia.settings.parm("Beams:eB", 10.);
    // Allow no substructure in e+- beams as we are neglecting
    // initial state radiation at low energy
  pythia.readString("PDF:lepton = off");
  pythia.init();

  // Begin event loop. Generate event. Skip if error. List first few.
  for (int iEvent = 0; iEvent < 10000; ++iEvent) {
    if (!pythia.next()) continue;

    pythia.event.list();

  // End of event loop. Statistics. Output histograms.
  }
  pythia.stat();
  return 0;
}
