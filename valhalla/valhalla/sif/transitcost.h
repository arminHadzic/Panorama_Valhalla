#ifndef VALHALLA_SIF_TRANSITCOST_H_
#define VALHALLA_SIF_TRANSITCOST_H_

#include <cstdint>
#include <valhalla/sif/dynamiccost.h>

/*
Armin H.
*/
#include <baldr/graphreader.h>
/*
Armin H.
*/


namespace valhalla {
namespace sif {

/**
 * Create a transit cost object.
 * @param  config  Property tree with configuration / options.
 */
cost_ptr_t CreateTransitCost(const boost::property_tree::ptree& config, baldr::GraphReader& graphreader);

}
}

#endif  // VALHALLA_SIF_TRANSITCOST_H_
