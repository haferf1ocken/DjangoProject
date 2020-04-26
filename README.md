Staging the docs

You have three options:

    On your local machine, clone this repo and run our staging container:

    git clone --recursive https://github.com/docker/docker.github.io.git
    cd docker.github.io
    docker-compose up

    If you haven't got Docker Compose installed, follow these installation instructions.

    The container runs in the background and incrementally rebuilds the site each time a file changes. You can keep your browser open to http://localhost:4000/ and refresh to see your changes. The container runs in the foreground, but you can use CTRL+C to get the command prompt back. To stop the container, issue the following command:

    docker-compose down

    Install Jekyll and GitHub Pages on your local machine.

    a. Clone this repo by running:

    git clone --recursive https://github.com/docker/docker.github.io.git

    b. Install Ruby 2.3 or later as described in Installing Ruby.

    c. Install Bundler:

    gem install bundler

    d. If you use Ubuntu, install packages required for the Nokogiri HTML parser:

    sudo apt-get install ruby-dev zlib1g-dev liblzma-dev

    e. Install Jekyll and other required dependencies:
