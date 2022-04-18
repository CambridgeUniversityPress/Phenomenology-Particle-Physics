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

// This is a simple test program to illustrate the effect of Lorentz boosts.

#include "Pythia8/Pythia.h"
using namespace Pythia8;
int main() {
  Pythia pythia;

  Vec4 P(0.,0.,0.,1.);
  cout << "Our first 4-vector : " << P << std::endl;

  // (1) boost along the x-direction forward and then backward
  double betax = 0.8;
  P.bst(betax,0,0);
  cout << "P after boost in x direction: " << P << std::endl;
  P.bst(-betax,0,0);
  cout << "P after boost in -x direction: " << P << std::endl;

  // (2) same along the y-direction forward and then backward
  double betay = 0.8;
  P.bst(0,betay,0);
  cout << "P after boost in y direction: " << P << std::endl;
  P.bst(0,-betay,0);
  cout << "P after boost in -y direction: " << P << std::endl;

  // (3) now combining boost along x and y directions
  P.bst(betax,0,0);
  P.bst(0,betay,0);
  cout << "P after boost in x and y direction: " << P << std::endl;
  P.bst(0,-betay,0);
  P.bst(-betax,0,0);
  cout << "P after boost reverse operations: " << P << std::endl;

  // (4) now combining boost along x and y directions but reversing
  the order of the backward boosts
  P.bst(betax,0,0);
  P.bst(0,betay,0);
    cout << "P after boost in x and y direction: " << P << std::endl;
  P.bst(-betax,0,0);
  P.bst(0,-betay,0);
  cout << "P after boost reverse operations in opposite order: " << P << std::endl;

  return 0;
}
