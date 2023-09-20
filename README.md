# Dimond HS Listings

The source code for the backend of the website [`Dimond HS Listings`](https://raventechnology.dev).

## Purpose

Dimond High School has had issues with properly communicating information about their clubs and events. So, this platform was designed to fix those issues. This website was designed for the DHS community to benefit from.

## Activity

This website will have been permanently shut down on 4 October 2023 at 16:30 AKDT. The activities director of Dimond High School, requested this website to be shut down, citing concerns of misinformation.

We have proper information checking policies in place. Despite our policies, Dimond HS still wants us to shut this website down. We are willing to work Dimond High School, but we will honor their request.

Raven Technology has done everything that we can in order to make sure that this website would have met the needs of Dimond High School. We hope that Dimond High School can model off of this code, so they can create their own platform, so that the members of Dimond High School has easier access to information.

## Installation

### Manual installation

For hosting, we used Ubuntu 22.04. If you're using a different server OS, you may have to modify these directions.

First, create the server, and get it running.

Clone the repo by running

`git clone https://github.com/raven-technology-dev/DHS_Listing.git`

Change drectory into the file by running:

`cd DHS_Listing`

Then, run this bash file, which installs and configures most dependancies.

`bash setup.bash`

Then, setup Postgres, by running:

`sudo -u postgres psql`

Once you're in the Postgres CLI, run (or run a modified version of this):

```
CREATE DATABASE <database_name>;
CREATE USER <user_name> WITH PASSWORD '<password>';
ALTER ROLE <user_name> SET client_encoding TO 'utf8';
ALTER ROLE <user_name> SET default_transaction_isolation TO 'read committed';
ALTER ROLE <user_name> SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE <database_name> TO <user_name>;
\q
```

Enter the relevant information into the `env` file.

Get yourself using the venv by running:

`
source .venv/bin/activate
`

Then, run:
`bash r.bash`
and then access the server at [`127.0.0.1:8000`](http://127.0.0.1:8000).

## Reason for open sourcing this.

We open sourced this, so our work wouldn't go to waste, and so it could do some good for other developers. We also hope that Dimond High School could use some of the code here, so they can create their own platform, so the community has easy access to information.

## Developers

[Raven Technology](https://raventechnology.dev) developed this website, to benefit the community. If you are interested in our development services, feel free to [Contact Us](https://raventechnology.dev/about/contact/) for a free consultation, or for more information.

## Notes

- We may add Docker support in the future.

- We were planning on adding tests, but since the platform got shut down, we have not added them yet.

- As the code indicates, there are many things that we planned on doing to make the UI less buggy. Unfortuantely, since we have stopped working on this, we are not going to impliment those things right now.
