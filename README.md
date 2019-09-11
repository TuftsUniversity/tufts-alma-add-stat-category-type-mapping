# tufts-alma-add-stat-category-type-mapping

**This script is in draft form, simply to help people import large sets of statistical categories and types in the stat category/Type mapping table.   As such, you may have to start and stop the script multiple times to complete the process.  Make sure to save the table each time if you run into errors.**  
<a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/">Creative Commons Attribution-NonCommercial 4.0 International License</a>.

**Title:**      Add statistical category and type mappings to Alma table

**Author:**     Henry Steele, Library Technology Services, Tufts University

**Date:**        September 2019

**Purpose:**

Automate input of statistical category and mapping table, that doesn't have an import function, with the Python Selenium web driver



**Input:**

The input file, which the script will ask for in a file picker, needs to have the following fields, **with no header**, in a **tab-delimited** .txt file
  - <Statistical Category Description>
  - <Statistical Category Type> (likely all the same import)

The script will input this table and enter each value pair in the Add Row pop up iteratively.

**Process:**
  - First go into Alma, into this mapping table, and enter one of the values you want the script to enter as the new category type, with add row.
    This is necessary because I could not make the script choose the "Category Type" field, and so you have to do this so the sticky setting will stick when you go to enter the other values.
  - Go to this downloaded repositories directory, and run the command python3 fileInput.py
  - follow the prompt to select your input file
  - Don't touch your computer or mouse while the script is running
  - Wait for it to complete or hang
  - Try saving the table
  - **If it won't save because of duplicate values, export the table to Excel and highlight duliplicates to find out which ones to remove.

**Note: I don't have the script save the changes.  You will need to do this at the end manually.  See note above**