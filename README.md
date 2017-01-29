# Russian_rhyme_detector
Python module for Russian rhyme detection

## How to use
1. Download the files
2. Project structure should look like this:
    ```
    .
    +-- rhyme_detect
    |   +-- _init_.py
    |   +-- extract.py
    |   +-- transcribe.py
    |   +-- yo_words.txt
    +-- folder_with_txt_files (e.g. test_folder)
    |   +-- test.txt
    |   +-- test2.txt
    |   +-- ...
    +-- my_rd.py
    ```
    
3. Go to my_rd.py file
4. Change the path to the folder with files or to the path of a file you want to analyze. 
   The files should have format *.txt. 
   You can also analyze files from the Russian National Corpus (RNC).
5. Make sure that your text files contain stress within the last words of the lines. 
   For marking stress please use the sign \` (Grave Accent U+0060) just after the stressed vowel.
   Words with the letter ё and one syllable words may be omit. 
   
   NB! If you write е instead of ё in the words like елка, you should either put an accent there or replace it with ё
6. If you analyze poems written before the year 1828, please uncomment the line 11 in my_rd.py.
   If you analyze a folder with files, you should have them all written either before or after the year 1828 to get more accurate results.
   Some important rhymes would be missing if you would not do it.
   
   E.g. the rhyme _безнаде\`жной - не\`жной_ from А.С. Пушкин. К \*\*\* («Я помню чудное мгновенье...») (1827) by default would not be recognized, because the transcription of _безнаде\`жной_ will be [б'ьзнад'о\`жнъj], as in modern pronunciation.
   
   Read more about the е/ё issue [here](https://avonizos.github.io/e_vs_yo/) (in Russian).
7. Run my_rd.py
8. Results will be shown in the parsed.csv file (rhymes and their classification)
   
### Note:
- The program does not take into account the stanzas' breaks. It is made so in order to be more flexible with the poems of complex structure. 
Simply structured rhymes can be analyzed by filtering the parsed.csv table by the column rhyming.
E.g. to get the correct rhymes from the Pushkin's example you may unable all the lines with - in the column rhyming.

- This project continues my BA thesis:
  
  [BA thesis git project](https://github.com/avonizos/BA_Thesis)
  
  [BA thesis text](https://www.hse.ru/en/edu/vkr/183946227) (Full text in Russian)
