
# COURSE GENERATION PIPELINE

## PLAN OF ACTION

### Step 1 - read 01-prompts/generate-structure-prompt.md
1. search online to find other 2 or 3 similar degree modules 
2. review their public facing content
3. donwload and save any specs if accessible
4. when making notes and saving them make sure to record the source URLs as well
  
### Step 2 - read 01-prompts/generate-structure-prompt.md
1. generate a module outline
2. save the module outline in '03-outline/'
3. generate a grapviz dot file which shows the module, outline, units, segments and learning outcomes of the course as a tree, rankdir LR, save it in 02-outline/course-structure.dot

### Step 3 - read 01-prompt/assessmentbrief-prompt.md
1. generate the assessment brief
2. save the the assessment brief in '04-assessment/assessment-brief.md'
3. generate a staff facing marking guidance
4. save the the assessment brief in '04-assessment/marking-guidance-STAFF.md'
5. generate a student facing marking rubric 
6. save the the assessment brief in '04-assessment/marking-rubric-STUDENT.md'
7. confirm that all 3 are consistant with each other

### Step 4 - Review and Approval

**Setup:**
1. create `04-review/v1/` and copy all files from `03-outline/` and `03-assessment/` into it
2. create `04-review/REVIEW.md` using the template below — one row per file, all statuses set to `REVIEWING`
3. notify the human that `04-review/REVIEW.md` is ready and explain how to use it

**REVIEW.md template:**
```
| File | Status | Feedback |
|------|--------|----------|
| 01-introduction.md | REVIEWING | |
| 02-search-and-pathfinding.md | REVIEWING | |
| ... (one row per outline unit) |
| assessment-brief.md | REVIEWING | |
| marking-guidance-STAFF.md | REVIEWING | |
| marking-rubric-STUDENT.md | REVIEWING | |
```
Statuses:
- `REVIEWING` — not yet assessed
- `REVISE` — human has written feedback; AI must revise
- `APPROVED` — human is satisfied; ready to roll out

**Feedback loop** (repeat until all rows are `APPROVED`):
1. pause and wait for the human to update `04-review/REVIEW.md`
2. for each row marked `REVISE`: read the feedback, revise the file, save it into a new `04-review/vN/` subfolder (incrementing N per revision round), reset that row's status to `REVIEWING` in `REVIEW.md`
3. for each row marked `APPROVED`: immediately copy that file into `05-approved/` and remove the row from `REVIEW.md`
4. summarise all changes made and ask the human to continue reviewing remaining files

Units in `05-approved/` are ready for Step 5 and may be progressed individually — Step 5 does not need to wait for all units to be approved.

### Step 5 - read 01-prompt/lectorialcontent-prompt.md
1. 
