const deleteNote = function(noteId){
    console.log(`삭제할 메모리 id ${noteId}`)

    // 전달할 데이터
    let note = {
        noteId : noteId
    }

    // 삭제 ajax
    fetch('/delete-note',{
        method : 'POST',
        body : JSON.stringify(note),
        headers : {
            "Content-Type" : "application/json"
        },
    }).then((response)=>response.json())
    .then(()=>{
        window.location.href = '/'; // 새로고침
    })
}