import pkg_resources

##### FILE #####

qc_file = 'resources/qc_files.txt'

##### PATH #####

qc_file_path = pkg_resources.resource_filename('squire', qc_file)
