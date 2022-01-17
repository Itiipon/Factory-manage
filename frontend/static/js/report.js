document.getElementById('startdate').onchange = (e)=>{
    const stop = document.getElementById('enddate').value 
    if (e.target.value){
        const requestOptions = {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                start:e.target.value,
                stop:stop
            }),
        };
        fetch('/api/report',requestOptions)
        .then(res => res.json())
        .then(data => {
            console.log(data)
            document.getElementById('work').innerHTML = data.minute + ' minute'
            document.getElementById('ot').innerHTML = data.ot + ' bath'
            document.getElementById('amount').innerHTML = data.amount + ' bath'
        })
    }  
}

document.getElementById('enddate').onchange = (e)=>{
    const start = document.getElementById('startdate').value 
    if (e.target.value){
        const requestOptions = {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                start:start,
                stop:e.target.value
            }),
        };
        fetch('/api/report',requestOptions)
        .then(res => res.json())
        .then(data => {
            document.getElementById('work').innerHTML = data.minute + ' minute'
            document.getElementById('ot').innerHTML = data.ot + ' bath'
            document.getElementById('amount').innerHTML = data.amount + ' bath'
        })
    }  
}