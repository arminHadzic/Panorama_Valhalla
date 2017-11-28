#include "midgard/logging.h"
#include "sif/dynamiccost.h"

#include "meili/universal_cost.h"

namespace valhalla {

namespace meili {


class UniversalCost : public sif::DynamicCost
{
 public:
  //Armin H.
  UniversalCost(const boost::property_tree::ptree& pt, baldr::GraphReader& graphreader)
      : DynamicCost(pt, graphreader, kUniversalTravelMode) {}

  bool Allowed(const baldr::DirectedEdge* edge,
               const sif::EdgeLabel& pred,
               const baldr::GraphTile*& tile,
               const baldr::GraphId& edgeid) const override
  {
    // Disable transit lines
    if (edge->IsTransitLine()) {
      return false;
    }
    return true;
  }

  uint32_t access_mode() const override {
    return 0;
  }

  bool AllowedReverse(const baldr::DirectedEdge* edge,
                      const sif::EdgeLabel& pred,
                      const baldr::DirectedEdge* opp_edge,
                      const baldr::GraphTile*& tile,
                      const baldr::GraphId& edgeid) const override
  { return true; }

  bool Allowed(const baldr::NodeInfo* node) const override
  { return true; }

  sif::Cost EdgeCost(const baldr::DirectedEdge* edge) const override
  {
    float length = edge->length();
    return { length, length };
  }

  // Disable astar
  float AStarCostFactor() const override
  { return 0.f; }

  virtual const sif::EdgeFilter GetEdgeFilter() const override
  {
    //throw back a lambda that checks the access for this type of costing
    return [](const baldr::DirectedEdge* edge){
      // Disable transit lines
      if (edge->IsTransitLine()) {
        return 0.f;
      }
      return 1.f;
    };
  }

  virtual const sif::NodeFilter GetNodeFilter() const override
  {
    //throw back a lambda that checks the access for this type of costing
    return [](const baldr::NodeInfo* node){
      // Do not filter any nodes
      return false;
    };
  }
};


//Armin H.
sif::cost_ptr_t CreateUniversalCost(const boost::property_tree::ptree& config, baldr::GraphReader& graphreader)
{ return std::make_shared<UniversalCost>(config, graphreader); }

}

}
