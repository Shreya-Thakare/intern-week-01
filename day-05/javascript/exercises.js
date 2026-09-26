// Day 5 JavaScript practice: reusable solutions.
const reverseString = text => [...text].reverse().join('');
const isPalindrome = text => { const clean=text.toLowerCase().replace(/[^a-z0-9]/g,''); return clean===reverseString(clean); };
const secondLargest = values => [...new Set(values)].sort((a,b)=>b-a)[1];
const frequency = text => [...text].reduce((out,char)=>({...out,[char]:(out[char]||0)+1}),{});
const firstNonRepeating = text => [...text].find(char => frequency(text)[char]===1) ?? null;
console.log({reverse:reverseString('intern'), palindrome:isPalindrome('Madam'), secondLargest:secondLargest([4,9,2,9,7]), frequency:frequency('hello'), first:firstNonRepeating('swiss')});
