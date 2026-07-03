docker run -it --publish 4000:4000 --volume="$PWD:/srv/jekyll:Z" --rm jekyll/jekyll:3.8 jekyll serve
