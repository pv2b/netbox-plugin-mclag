from setuptools import find_packages, setup

setup(
    name='netbox-plugin-mclag',
    version='0.1.1',
    description='Manage Multi-Chassis Link Aggregation Groups in Netbox (MC-LAG / MLAG / vPC / etc)',
    install_requires=[],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)
