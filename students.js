/**
 * Each week, a class of students sits an test. They sit in a single
 * row, in the same order every week.
 *
 * When a student takes the test, if both students they sit next
 * to scored higher than them on last week's test, that student
 * will score 1 higher on this week's test. Conversely, if both
 * stuents they sit next to scored lower than them last week,
 * they will score 1 lower this week. A stuend who sits at the
 * end of the row will not change their test score.
 * 
 * The students stop taking tests when every student scores the
 * same as they did the previous week.
 *
 * Write a function that, given an initial array of positive integer
 * student test scores, will return the test scores of each student
 * once they stop taking tests.
 */

var step = function(state) {
    // There must be at least 1 student between 2 other students
    var newRow = Array.from(state.row);
    var left, right;
    state.changed = false;

    for(var i = 1; i<state.row.length-1; i++){
        left = state.row[i-1];
        right = state.row[i+1];
        current = state.row[i];
        if(left > current && right > current){
            newRow[i] = current + 1;
            state.changed = true;
        } else if (left < current && right < current) {
            newRow[i] = current - 1;
            state.changed = true;
        } else {
            newRow[i] = current;
        }
    }

    state.row = newRow;
    return state;
}

function solution(row) {
    if(row.length < 3){
        return row;
    }

    var state = {
        row: row,
        changed: true
    };

    while(state.changed) {
        state = step(state);
    }

    return state.row;
}
