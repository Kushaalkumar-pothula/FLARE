from concurrent.futures import ProcessPoolExecutor


def runFile(filename):
    exec(open(filename).read())


if __name__ == '__main__':
    with ProcessPoolExecutor() as e:
        [e.submit(runFile, i) for i in ['distance.py', 'energy.py']]

    runFile('fluence.py')

    with ProcessPoolExecutor() as e:
        [e.submit(runFile, i) for i in ['fluence_analysis.py', 'fluence_x_rays.py']]
