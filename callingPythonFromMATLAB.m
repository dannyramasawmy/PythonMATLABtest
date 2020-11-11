%% callingPythonFromMATLAB

% point matlab to python
pyenv('Version','C:\ProgramData\Anaconda3\python.exe')
 
% view python environment (can be changed)
pyenv


% use built in python classes
% list
mylist = py.list();
for idx = 1:10
    mylist.append(idx)
end
disp(mylist)


% dictionaries
mydict = py.dict();
text = {'hello', 'world', 'and', 'other', 'things',44,55,'like','numbers'};
for idx = text
    % word : length(word)
   mydict{idx{:}} = length(idx{:});
end
disp(mydict)


% python libraries / user modules 

% calling simple functions - repeat text
out = py.MyLibrary.repeatText(4, "4 x hello! ");
disp(out)

% calling simple functions - count letters
inp_text = 'the quick brown fox jumped over the lazy dog.';
out = py.MyLibrary.countLetters(inp_text);
disp(out)

% calling classes
myPB = py.MyLibrary.PhoneBook();
myPB.add('John', '0123456');
myPB.add('Jane', '0133156');
myPB.add('Jo', '0126456');
myPB.add('Jo', '0126456');
myPB.add('Jo', '0123333');
disp(myPB);
myPB.ring('Jo');


