# ExampleRepo
Example Repository for learning Git basics.

## Setup
Setup this repo for your own:

1. Clone the repo to your local machine:

```
git clone https://github.com/Jan-Meyer01/ExampleRepo
```

The following are already done for this, but for a new repo the next steps would be:

2. Copy your code from whatever folder into the repo folder called 'ExampleRepo'.

3. Commit your old code:

```
git add . 
git commit -m "Added old code"
```

4. Push your commit to the remote repo:

```
git push
```

## Git Workflow
Next we want to look at the typical Git workflow and how we can change our code. There are a couple problems with the repo as it is now:

First, the python script `DummyDataReader.py` takes in arguments for in and ouput folders, but has no argument for the file name. We firstly need to add this argument to the parser:

```
parser.add_argument('-n','--name', default='DummyData', help='name of the data')
```

In VSCode, this line will then be highlighted with green next to the line number on the left as its completly new. Then we need to change the loading and saving to incorporate the new variable:

```
data = loadmat(join(path_input,args.name+'.mat'))
np.save(join(path_output,args.name), data)
```
    
These changes will be shown in blue marking a change in already existing code. The Code should still work as before with the default values, but can now be called with more functionality from the terminal.

To truly test this change, we can rename `DummyData.mat` or change the file name in `DummyDataGenerator.m` and generate a new `.mat` file. Then we call our script from the command line and add our new name with the `-n` argument that we just added. This could look something like this if we renamed the data to `NewDummyData.mat` (note that in VSCode an R for renamed will appear next to the file once added):

```
python DummyDataReader.py -n NewDummyData
```

Note that you might need to write the exact environment instead of just python depending on your setup.
    
Now we can follow the steps 3 and 4 from above with an appropiate commit message to save our changes.

Second, as you will have seen at the end of the last we added new data to our remote. Thus we have data in our repo, which we will keep on committing. This, however, is not optimal as our repo keeps growing and we may be unintentionally sharing sensitive data. To stop this from happening, we can create a `.gitignore` file (ideally we would have done this right at the beginning) where we put the name of the data folder and any other annoying files that might be created as a sideproduct of our coding. Our `.gitignore` would thus simply look like this:

```
data
```

Simple, right? Well, as the data folder was already added in a commit before we need to do some extra steps in order to remove the data from our remote and ignore it for future commits. Write the following command and then add all files and commit in order to get the data removed:

```
git rm -r --cached data
```    
    
Now, at least in VSCode, the files should be grayed out indicating that they are being ignored. Even if you now write `git add . ` to add everything to the index these files will not be added. To test this further you can delete a file from the `data` folder and look with `git status` whether it is shown as deleted. You can also create a new folder, put it into the `.gitignore` and this time it should work without any problems as that folder was not previously commited!

An important thing to consider is that you rarely work alone in a repo. In case other people also work on the same code as you make sure to always use `git pull` to stay up to date and avoid merge conflicts, especially before pushing new code to the remote.