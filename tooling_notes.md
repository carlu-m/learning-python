# Notes on creating a project from scratch

## Create the github project

## Install UV globally

Install `uv` globally on the system, for Manjaro:

```
    sudo pacman -S python-uv
```

Then in the folder of your future project (beware this will remove everything else):

```
    uv init .
```

Or if the folder does not exist yet:

```
    uv init <name-of-your-project>
```

This will create some basic files for the project

##