#include "test.h"

#include "sif/costfactory.h"
#include "sif/autocost.h"
#include "sif/pedestriancost.h"
#include "sif/bicyclecost.h"

/*
Armin H.
*/
#include "baldr/graphreader.h"
/*
Armin H.
*/

using namespace std;
using namespace valhalla::sif;

namespace {
  void test_register() {
    CostFactory<DynamicCost> factory;
    factory.Register("auto", CreateAutoCost);
    factory.Register("auto_shorter", CreateAutoShorterCost);
    factory.Register("bicycle", CreateBicycleCost);
    factory.Register("pedestrian", CreatePedestrianCost);
    //TODO: then ask for some
    //Armin H.
    boost::property_tree::ptree pt;
    pt.put("tile_dir", "test/gphrdr_test");
    valhalla::baldr::GraphReader reader(pt);
    auto car = factory.Create("auto", pt, reader);
  }
}

int main(void)
{
  test::suite suite("factory");

  suite.test(TEST_CASE(test_register));
  //TODO: many more

  return suite.tear_down();
}
