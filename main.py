from os import path, mkdir
from datetime import datetime
from concurrent.futures import ProcessPoolExecutor

from distance import generate_distance
from energy import generate_energy
from fluence import generate_fluence
from fluence_analysis import generate_fluence_plot
from fluence_x_rays import generate_fluence_xray


if __name__ == '__main__':
    time_now = datetime.now().strftime("%Y-%m-%d-%H-%M")
    dirname = f'results_{time_now}'
    if not path.exists(dirname):
        mkdir(dirname)

    with ProcessPoolExecutor() as e:
        e.submit(generate_distance, dirname)
        e.submit(generate_energy, dirname)

    generate_fluence(dirname)

    with ProcessPoolExecutor() as e:
        e.submit(generate_fluence_plot, dirname)
        e.submit(generate_fluence_xray, dirname)
