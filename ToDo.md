# Project Ideas/To Do's

## Features

* Allow user uploaded content
  * Need to limit types and keep secure
  * Need to store securely
  * Best approach?
  * Need backups/restores then?  Consistency with database references?
  * When to store locally (filesystem) versus object storage like S3?
  * Does it ever make sense to use a database and which one(s)?
* Paging (only display 10/configurable amount of content at a time)
* Filtering (only display selected content)
* Search
* Markdown and/or WYSIWIG/Rich-text-editing support
* Add API endpoint for each view
  * Support JSON and XML content-types
* Fix Leaderboard report so it sorts by score
  * Allow changing sort order by clicking on column headers and a default option to resotre the sort
* Add user types
* Add staff users who can MAC paths and moderate user posts

## Scaling

* Use Redis instance for caching?
* Use CDN like Cloudflare?
* Use ads to offset costs
  * AWS Affiliate ads
  * Ethical ads/other platforms

## Infrastructure

* Use docker?
  * Re-visit when have version of Windows 10 that supports it alongside VMware Workstation
* Automated build process?
* Migrate to AWS?
  * But must figure out how to cap costs
* Look at analytics - probably Google Analytics
