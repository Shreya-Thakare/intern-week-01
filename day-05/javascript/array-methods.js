const employees=[{name:'Asha',salary:65000,department:'Engineering'},{name:'Ravi',salary:48000,department:'HR'},{name:'Neha',salary:72000,department:'Engineering'}];
const engineering=employees.filter(employee=>employee.department==='Engineering');
const names=employees.map(employee=>employee.name);
const highestPaid=employees.reduce((best,employee)=>employee.salary>best.salary?employee:best);
const averageSalary=employees.reduce((sum,employee)=>sum+employee.salary,0)/employees.length;
console.log({engineering,names,highestPaid,averageSalary});
