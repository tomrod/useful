import numpy as np


def body_mass_index(height, weight, metric='metric'):
    '''
    body_mass_index: calculate BMI. Supports ['metric','imperial'] units.

    Inputs: 
        height: numeric, height in inches or meters
        weight: numeric, weight in pounds or kilograms
        metric: string, one of 'metric' or 'imperial'

    Output:
        Numeric, BMI
    '''

    if metric == 'imperial':
        h_coeff = 0.0254 #inches -> meters
        w_coeff = 0.453592 #pounds -> kilogram
    elif metric == 'metric':
        h_coeff = 1
        w_coeff = 1
    else:
        raise ValueError('Metric must be in [\'imperial\',\'metric\']')

    h = h_coeff * height
    w = w_coeff * weight

    return np.round(w / (h*h), 2)
    
