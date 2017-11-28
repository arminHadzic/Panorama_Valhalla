// -*- mode: c++ -*-
#ifndef MMP_MAP_MATCHER_FACTORY_H_
#define MMP_MAP_MATCHER_FACTORY_H_
#include <cstdint>

#include <string>

#include <boost/property_tree/ptree.hpp>

#include <valhalla/sif/costconstants.h>
#include <valhalla/sif/costfactory.h>
#include <valhalla/baldr/graphreader.h>

#include <valhalla/meili/candidate_search.h>
#include <valhalla/meili/map_matcher.h>


namespace valhalla {
namespace meili {

class MapMatcherFactory final
{
public:
  MapMatcherFactory(const boost::property_tree::ptree&);

  ~MapMatcherFactory();

  baldr::GraphReader& graphreader()
  { return graphreader_; }

  CandidateQuery& candidatequery()
  { return candidatequery_; }

  MapMatcher* Create(const std::string& name)
  { return Create(name, boost::property_tree::ptree()); }

  MapMatcher* Create(const std::string& name,
                     const boost::property_tree::ptree& preferences);

  MapMatcher* Create(const boost::property_tree::ptree&);

  boost::property_tree::ptree
  MergeConfig(const std::string&, const boost::property_tree::ptree&);

  void ClearFullCache();

  void ClearCache();

  static constexpr size_t kModeCostingCount = 8;

private:
  //Armin H. changed so all costs require a graph reader input, since variable arguments cannot be done with dynamic typing without significantly changing the code base.
  //OLD: typedef sif::cost_ptr_t (*factory_function_t)(const boost::property_tree::ptree&);
  typedef sif::cost_ptr_t (*factory_function_t)(const boost::property_tree::ptree& config, baldr::GraphReader& graphreader);
  //Armin H.

  boost::property_tree::ptree config_;

  baldr::GraphReader graphreader_;

  valhalla::sif::cost_ptr_t mode_costing_[kModeCostingCount];

  sif::CostFactory<sif::DynamicCost> cost_factory_;

  CandidateGridQuery candidatequery_;

  float max_grid_cache_size_;

  sif::cost_ptr_t get_costing(const boost::property_tree::ptree& request, const std::string& costing, baldr::GraphReader& graphreader);
};

}
}

#endif // MMP_MAP_MATCHER_FACTORY_H_
