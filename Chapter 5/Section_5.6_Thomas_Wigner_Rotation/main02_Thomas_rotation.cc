/***
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% P3: Phenomenology of Particle Physics
%%
%% Author:  André Rubbia
%%
%% Section 5.5 Thomas-Wigner Rotation
%%
%% This work is licensed under the Creative Commons Attribution 4.0 International License.
%% To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/ or
%% send a letter to Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.
%%
%% PYTHIA is licenced under the GNU GPL v2 or later.
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
**/

// This is a simple test program to illustrate the existence of the Thomas-Wigner rotation

#include "Pythia8/Pythia.h"
using namespace Pythia8;
int main() {
  Pythia pythia;

  Vec4 Pxy(0.,0.,0.,1.);
  Vec4 Pyx(Pxy);
  double beta = 0.8;
  Pyx.bst(beta,0,0);
  Pyx.bst(0,beta,0);
  cout << "P after boost in x then y direction: " << Pyx << std::endl;
  Pxy.bst(0,beta,0);
  Pxy.bst(beta,0,0);
  cout << "P after boost in y then x direction: " << Pxy << std::endl;
  double cosT = 2*sqrt(1-beta*beta)/(2-beta*beta);
  double thetaT = acos(cosT);
  Pxy.rotaxis(thetaT, 0,0,1);
  cout << "after Thomas rotation : " << Pxy << std::endl;

  return 0;
}
