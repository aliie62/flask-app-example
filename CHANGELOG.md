
# Change Log
All notable changes to this project will be documented in this file.
 
The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).
 

 
## [1.0.1] - 2022-04-06
 
### Added
- Changelog
   
### Changed
- Moved out db app initiation from the file name check if block in app.py.
- Python version to 3.9.12
 
### Fixed
- Beoken Flask-JWT-Extended decorators due to recent of improvements of this package; more information here: [Breaking Changes and Upgrade Guide](https://flask-jwt-extended.readthedocs.io/en/stable/v4_upgrade_guide/)
- Bug in save_to_db method of UserModel

## Removed
- Unnecessary commented codes
- run.py (for cloud host impplementation)
- uwsgi.py (for cloud host impplementation)
- Procfile (for cloud host impplementation)


