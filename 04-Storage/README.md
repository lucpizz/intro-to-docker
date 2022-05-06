# Docker Storage

Storage Drivers are used to store data in a container.

## Storage Models

Persistent data cans be manafed using several storage models.

File System:
- Data is stored in a file system.
- Data is stored in a directory.
- Efficient use of memory.
- Inefficient use for write-heavy-workloads

Block Storage:
- Stores data in blocks
- Used by devicemapper
- Efficient with write heavy workloads

Object Storage:
- Stores data in objects
- APplication must be desighed to use object base storage.