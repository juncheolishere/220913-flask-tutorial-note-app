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

//  상수 및 변수
const modal = new bootstrap.Modal('#updateNoteModal');
let updateNoteId; // 현재 수정 중인 메모

const showUpdateNoteModal = function(noteId){
    console.log(`형재 클린된 메모 id ${noteId}`)

    // 현재 수정할 메모 반영
    updateNoteId = noteId

    // Modal show
    modal.show();
}

const updateNote = function(){
    console.log(1)
    let updateTitle = document.querySelector('#update-title'); // 현재 수정할 메모의 제목
    let updateContent = document.querySelector('#update-content'); ; // 현재 수정할 메모의 내용

    // 전달할 데이터 정보(수정 메모 정보)
    let note = {
        noteId : updateNoteId,
        title : updateTitle.value,
        content : updateContent.value,
    }

    console.log(note)

    // 수정 ajax
    fetch('/update-note',{
        method : 'PUT',
        body : JSON.stringify(note),
        headers: {
            "Content-Type": "application/json"
        },
    }).then((response) => response.json())
    .then(()=>{
        window.location.href = '/'; // 새로고침
    });
}