def get_kernel_suite(n_dims, ls_bounds=(1e-3, 1e8), noise_bounds=(1e-10, 1e2)):
    """
    Dynamically creating an ablation kernel dictionary adapted to input dimension (n_dims)
    """
    init_ls_ard = [0.1] * n_dims
    
    return {
        "Baseline: Matern 2.5 + WhiteNoise (ARD)": (
            Matern(length_scale=init_ls_ard, nu=2.5, length_scale_bounds=ls_bounds) +
            WhiteKernel(noise_level=1e-3, noise_level_bounds=noise_bounds)
        ),
        "Ablation 1: Matern 1.5 + WhiteNoise (Rougher/Spiky)": (
            Matern(length_scale=init_ls_ard, nu=1.5, length_scale_bounds=ls_bounds) +
            WhiteKernel(noise_level=1e-3, noise_level_bounds=noise_bounds)
        ),
        "Ablation 2: RBF + WhiteNoise (Smooth Gaussian)": (
            RBF(length_scale=init_ls_ard, length_scale_bounds=ls_bounds) +
            WhiteKernel(noise_level=1e-3, noise_level_bounds=noise_bounds)
        ),
        "Ablation 3: Rational Quadratic + WhiteNoise": (
            RationalQuadratic(length_scale=0.1, alpha=1.0) +
            WhiteKernel(noise_level=1e-3, noise_level_bounds=noise_bounds)
        ),
        "Ablation 4: Matern 2.5 WITHOUT WhiteNoise (Noiseless)": (
            Matern(length_scale=init_ls_ard, nu=2.5, length_scale_bounds=ls_bounds)
        ),
        "Ablation 5: Matern 2.5 Isotropic (Shared Lengthscale)": (
            Matern(length_scale=0.1, nu=2.5, length_scale_bounds=ls_bounds) +
            WhiteKernel(noise_level=1e-3, noise_level_bounds=noise_bounds)
        )
    }
