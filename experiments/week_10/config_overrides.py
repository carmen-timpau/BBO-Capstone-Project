# Configurations file with global defaults and function-specific overrides used in Week 10 BBO Pipeline
# Overrides were identified in pre-production, during manual pipeline evaluation and troubleshooting

# Global Defaults
n_init_base = 5
init_per_dim = 2
n_iterations = 15
n_seeds = 500
holdout_fraction = 0.3

# Function-specific Overrides
n_init_base_overrides={
            "function_1": 4, 
            "function_2": 4
        }

init_per_dim_overrides={
            "function_4": 1, 
            "function_5": 1, 
            "function_6": 1,
            "function_7": 1, 
            "function_8": 1
        }

holdout_fraction_overrides={
            "function_1": 0.6,
            "function_2": 0.6,
            "function_5": 0.15,
            "function_8": 0.15
        }

n_seeds_overrides={
            "function_1": 1000, 
            "function_2": 1000,
            "function_3": 500, 
            "function_4": 500, 
            "function_5": 500,
            "function_6": 500, 
            "function_7": 500, 
            "function_8": 500
        }
