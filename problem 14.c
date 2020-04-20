//GSL FUNCTIONS FOR BOUNDARY VALUED PROBLEMS:
//REFERENCE: https://www.gnu.org/software/gsl/doc/html/ode-initval.html
/*
 1. Adaptive size control:   
    gsl_odeiv2_control * gsl_odeiv2_control_standard_new(double eps_abs, double eps_rel, double a_y, double a_dydt)
 
 2. int gsl_odeiv2_step_apply(gsl_odeiv2_step * s, double t, double h, double y[], double yerr[], const double dydt_in[], double dydt_out[], const gsl_odeiv2_system * sys)
 
 3. making step:
     gsl_odeiv2_step * gsl_odeiv2_step_alloc(const gsl_odeiv2_step_type * T, size_t dim)
     int gsl_odeiv2_step_reset(gsl_odeiv2_step * s)
     void gsl_odeiv2_step_free(gsl_odeiv2_step * s)
     unsigned int gsl_odeiv2_step_order(const gsl_odeiv2_step * s)
     int gsl_odeiv2_step_apply(gsl_odeiv2_step * s, double t, double h, double y[], double yerr[], const double dydt_in[], double dydt_out[], const gsl_odeiv2_system * sys)
     
 4. gsl_odeiv2_driver * gsl_odeiv2_driver_alloc_y_new(const gsl_odeiv2_system * sys, const gsl_odeiv2_step_type * T, const double hstart, const double epsabs, const double epsrel)
 
 5.int gsl_odeiv2_driver_apply_fixed_step(gsl_odeiv2_driver * d, double * t, const double h, const unsigned long int n, double y[])
 */
 
 //Example from online::
 
 #include <stdio.h>
#include <gsl/gsl_errno.h>
#include <gsl/gsl_matrix.h>
#include <gsl/gsl_odeiv2.h>

int
func (double t, const double y[], double f[],
      void *params)
{
  (void)(t); /* avoid unused parameter warning */
  double mu = *(double *)params;
  f[0] = y[1];
  f[1] = -y[0] - mu*y[1]*(y[0]*y[0] - 1);
  return GSL_SUCCESS;
}

int
jac (double t, const double y[], double *dfdy,
     double dfdt[], void *params)
{
  (void)(t); /* avoid unused parameter warning */
  double mu = *(double *)params;
  gsl_matrix_view dfdy_mat
    = gsl_matrix_view_array (dfdy, 2, 2);
  gsl_matrix * m = &dfdy_mat.matrix;
  gsl_matrix_set (m, 0, 0, 0.0);
  gsl_matrix_set (m, 0, 1, 1.0);
  gsl_matrix_set (m, 1, 0, -2.0*mu*y[0]*y[1] - 1.0);
  gsl_matrix_set (m, 1, 1, -mu*(y[0]*y[0] - 1.0));
  dfdt[0] = 0.0;
  dfdt[1] = 0.0;
  return GSL_SUCCESS;
}

int
main (void)
{
  double mu = 10;
  gsl_odeiv2_system sys = {func, jac, 2, &mu};

  gsl_odeiv2_driver * d =
    gsl_odeiv2_driver_alloc_y_new (&sys, gsl_odeiv2_step_rk8pd,
                                  1e-6, 1e-6, 0.0);
  int i;
  double t = 0.0, t1 = 100.0;
  double y[2] = { 1.0, 0.0 };

  for (i = 1; i <= 100; i++)
    {
      double ti = i * t1 / 100.0;
      int status = gsl_odeiv2_driver_apply (d, &t, ti, y);

      if (status != GSL_SUCCESS)
        {
          printf ("error, return value=%d\n", status);
          break;
        }

      printf ("%.5e %.5e %.5e\n", t, y[0], y[1]);
    }

  gsl_odeiv2_driver_free (d);
  return 0;
}


//The user can work with the lower level functions directly, as in the following example. 
//In this case an intermediate result is printed after each successful step instead of equidistant time points.

//example: 2

int
main (void)
{
  const gsl_odeiv2_step_type * T
    = gsl_odeiv2_step_rk8pd;

  gsl_odeiv2_step * s
    = gsl_odeiv2_step_alloc (T, 2);
  gsl_odeiv2_control * c
    = gsl_odeiv2_control_y_new (1e-6, 0.0);
  gsl_odeiv2_evolve * e
    = gsl_odeiv2_evolve_alloc (2);

  double mu = 10;
  gsl_odeiv2_system sys = {func, jac, 2, &mu};

  double t = 0.0, t1 = 100.0;
  double h = 1e-6;
  double y[2] = { 1.0, 0.0 };

  while (t < t1)
    {
      int status = gsl_odeiv2_evolve_apply (e, c, s,
                                           &sys,
                                           &t, t1,
                                           &h, y);

      if (status != GSL_SUCCESS)
          break;

      printf ("%.5e %.5e %.5e\n", t, y[0], y[1]);
    }

  gsl_odeiv2_evolve_free (e);
  gsl_odeiv2_control_free (c);
  gsl_odeiv2_step_free (s);
  return 0;
}
