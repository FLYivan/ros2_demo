from setuptools import find_packages, setup
import os
from glob import glob


package_name = 'go2_description'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*.launch.py'))),
        (os.path.join('share', package_name, 'urdf'), glob(os.path.join('urdf', '*.*'))),
        (os.path.join('share', package_name, 'meshes'), glob(os.path.join('meshes', '*.*'))),
        (os.path.join('share', package_name, 'xacro'), glob(os.path.join('xacro', '*.*'))),   
        (os.path.join('share', package_name, 'config'), glob(os.path.join('config', '*.*'))), 
        (os.path.join('share', package_name, 'dae'), glob(os.path.join('dae', '*.*'))), 
        (os.path.join('share', package_name, 'world'), glob(os.path.join('world', '*.*'))), 
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*.rviz'))),
        (os.path.join('share', package_name, 'urdf/sensors'), glob(os.path.join('urdf/sensors', '*.*'))),

    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='flyivan',
    maintainer_email='luoyifan902008@126.com',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
