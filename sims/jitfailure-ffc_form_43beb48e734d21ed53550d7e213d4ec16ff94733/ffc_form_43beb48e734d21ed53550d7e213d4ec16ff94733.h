// This code conforms with the UFC specification version 2016.2.0
// and was automatically generated by FFC version 2016.2.0.
// 
// This code was generated with the following parameters:
// 
//   convert_exceptions_to_warnings: False
//   cpp_optimize:                   True
//   cpp_optimize_flags:             '-O2'
//   epsilon:                        1e-14
//   error_control:                  False
//   form_postfix:                   False
//   format:                         'ufc'
//   max_signature_length:           0
//   no-evaluate_basis_derivatives:  True
//   optimize:                       False
//   precision:                      100
//   quadrature_degree:              -1
//   quadrature_rule:                'auto'
//   representation:                 'auto'
//   split:                          False

#ifndef __FFC_FORM_43BEB48E734D21ED53550D7E213D4EC16FF94733_H
#define __FFC_FORM_43BEB48E734D21ED53550D7E213D4EC16FF94733_H
#include <ffc_element_06b84d8b0c4ba9118bfe4a715078a884675bdf94.h>
#include <ffc_element_4129196f8130ba84efe6cd7c83c851a8ca47d028.h>
#include <ffc_element_639eb2b6364c832bf001f46acc76381a1eeb07fa.h>
#include <stdexcept>
#include <ufc.h>

class ffc_form_43beb48e734d21ed53550d7e213d4ec16ff94733_exterior_facet_integral_main_1: public ufc::exterior_facet_integral
{
public:

  ffc_form_43beb48e734d21ed53550d7e213d4ec16ff94733_exterior_facet_integral_main_1();

  ~ffc_form_43beb48e734d21ed53550d7e213d4ec16ff94733_exterior_facet_integral_main_1() override;

  const std::vector<bool> & enabled_coefficients() const final override;

  void tabulate_tensor(double * A,
                       const double * const * w,
                       const double * coordinate_dofs,
                       std::size_t facet,
                       int cell_orientation) const final override;

};

extern "C" ufc::exterior_facet_integral * create_ffc_form_43beb48e734d21ed53550d7e213d4ec16ff94733_exterior_facet_integral_main_1();


class ffc_form_43beb48e734d21ed53550d7e213d4ec16ff94733_form_main: public ufc::form
{
public:

  ffc_form_43beb48e734d21ed53550d7e213d4ec16ff94733_form_main();

  ~ffc_form_43beb48e734d21ed53550d7e213d4ec16ff94733_form_main() override;

  const char * signature() const final override;

  std::size_t rank() const final override;

  std::size_t num_coefficients() const final override;

  std::size_t original_coefficient_position(std::size_t i) const final override;

  ufc::finite_element * create_coordinate_finite_element() const final override;

  ufc::dofmap * create_coordinate_dofmap() const final override;

  ufc::coordinate_mapping * create_coordinate_mapping() const final override;

  ufc::finite_element * create_finite_element(std::size_t i) const final override;

  ufc::dofmap * create_dofmap(std::size_t i) const final override;

  std::size_t max_cell_subdomain_id() const final override;

  std::size_t max_exterior_facet_subdomain_id() const final override;

  std::size_t max_interior_facet_subdomain_id() const final override;

  std::size_t max_vertex_subdomain_id() const final override;

  std::size_t max_custom_subdomain_id() const final override;

  std::size_t max_cutcell_subdomain_id() const final override;

  std::size_t max_interface_subdomain_id() const final override;

  std::size_t max_overlap_subdomain_id() const final override;

  bool has_cell_integrals() const final override;

  bool has_exterior_facet_integrals() const final override;

  bool has_interior_facet_integrals() const final override;

  bool has_vertex_integrals() const final override;

  bool has_custom_integrals() const final override;

  bool has_cutcell_integrals() const final override;

  bool has_interface_integrals() const final override;

  bool has_overlap_integrals() const final override;

  ufc::cell_integral * create_cell_integral(std::size_t i) const final override;

  ufc::exterior_facet_integral * create_exterior_facet_integral(std::size_t i) const final override;

  ufc::interior_facet_integral * create_interior_facet_integral(std::size_t i) const final override;

  ufc::vertex_integral * create_vertex_integral(std::size_t i) const final override;

  ufc::custom_integral * create_custom_integral(std::size_t i) const final override;

  ufc::cutcell_integral * create_cutcell_integral(std::size_t i) const final override;

  ufc::interface_integral * create_interface_integral(std::size_t i) const final override;

  ufc::overlap_integral * create_overlap_integral(std::size_t i) const final override;

  ufc::cell_integral * create_default_cell_integral() const final override;

  ufc::exterior_facet_integral * create_default_exterior_facet_integral() const final override;

  ufc::interior_facet_integral * create_default_interior_facet_integral() const final override;

  ufc::vertex_integral * create_default_vertex_integral() const final override;

  ufc::custom_integral * create_default_custom_integral() const final override;

  ufc::cutcell_integral * create_default_cutcell_integral() const final override;

  ufc::interface_integral * create_default_interface_integral() const final override;

  ufc::overlap_integral * create_default_overlap_integral() const final override;

};

extern "C" ufc::form * create_ffc_form_43beb48e734d21ed53550d7e213d4ec16ff94733_form_main();

#endif