# **PBP Assignment 6**

Nama : Carlene Annabel

NPM : 2106752211

Kelas :D

https://katalog-carlene.herokuapp.com/todolist/login/?next=/todolist/login

##  ** Jelaskan perbedaan antara asynchronous programming dengan synchronous programming**

Asynchronous programming merupakan sebuah pendekatan pemrograman yang tidak terikat pada input output (I/O)  protocol. Ini menandakan bahwa pemrograman asynchronous tidak melakukan pekerjaannya secara old style / cara lama yaitu dengan eksekusi baris program satu persatu secara hirarki. Asynchronous programming melakukan pekerjaannya tanpa harus terikat dengan proses lain atau dapat kita sebut secara Independent.
Berbeda dengan asynchronous, synchronous programming memiliki pendekatan yang lebih old style. Task akan dieksekusi satu persatu sesuai dengan urutan dan prioritas task. Hal ini memiliki kekurangan pada lama waktu eksekusi karena masing-masing task harus menunggu task lain selesai untuk diproses terlebih dahulu.

##  ** Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.**

Event-Driven Programming merupakan paradigma pemrograman yang terjadi bila ada event/kejadian. Pada tugas ini, misalnya jika ingin mensubmit modal form yang telah kita buat, kita melakukan proses POST yang kemudian akan memunculkan data kita.

## **Jelaskan penerapan asynchronous programming pada AJAX.**

AJAX secara bersamaan memulai permintaan JavaScript dan XML yang lebih mudah diurai. Dari sini, ini mengurangi waktu buka situs web sambil meningkatkan kinerja. Dengan AJAX menjalankan protokol HTTP pada link uniknya, ia mendapat akses ke semua kata kerja HTTP termasuk permintaan HEAD. Yang memungkinkan data diperbarui secara real-time dengan mulus. Dengan demikian, menghapus komunikasi sinkron sisi klien-ke-server default yang memerlukan proses untuk dijalankan secara berkala, dan seperti namanya – Asynchronus.

## ** Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas. **

1. Membuat view baru yang mengembalikan seluruh data task dalam bentuk JSON.

```js
def show_todolist_json(request):
    task = Task.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", task), content_type="application/json")
```

2. Membuat path /todolist/json yang mengarah ke view yang baru.

```js
    path('json/', show_todolist_json,name='show_todolist_json'),
```

3. Fungsi untuk pengambilan task pada todolist.html

```js
function showJson(){
        $.get("/todolist/json/", function(data){
            for(i = 0; i < data.length; i++){
                addText(data[i].fields.title, data[i].fields.description, data[i].fields.is_finished, data[i].fields.date, data[i].fields.pk)
            }
        })
    }
```

4. Membuat tombol add task

5. Membuat  view baru untuk menambahkan task baru ke dalam database.

```js
def create_task_ajax(request):
     if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        user = request.user
        date = datetime.datetime.now()
        is_finished = False
        item = Task(title=title, description=description, user=user, date=date, is_finished=is_finished)
        item.save()
        return JsonResponse({"Message": "Task Success"},status=200)
```

6. Membuat path /todolist/add yang mengarah ke view baru.

```js
    path('add/', create_task_ajax, name = 'create_task_ajax'),
```

7. Menghubungkan  form yang telah  dibuat di dalam modal ke path /todolist/add dan menuptupnya setelah penambahan task berhasil dan refresh secara asinkronus dengan membuat function makeCards() untuk menambahkan data secara asinkronus dan submitTask() untuk submit form task ke database

```js
function makeCards(){
        let text= "";
        $.ajax({
            url: "{% url 'todolist:show_todolist_json' %}",
            type: "GET",
            dataType: "json",
            success: function(data){
                for(let task of data){
                    text += `<div class="m-2 card p-2">
                        <p class="text font-weight-bold">Task : ${task.fields.title}</p>
                        <p>Description : ${task.fields.description}</p>
                        <p>Created : ${task.fields.date}</p>
                        <p>Status : 
                            <span class=" ${task.fields.is_finished ? 'text-danger unfinished':'text-success finished'}">
                                ${task.fields.is_finished ? 'Completed':'Unfinished'}
                            </span>
                        </p>
                        <button class="btn" ><a><i class="fa fa-trash"></i></a></button>
                        <input class='todolist-check' 
                                        type="checkbox" 
                                        id='${task.pk}' 
                                        value= '${task.pk}'
                                        name="finishbtn"
                                        ${task.fields.is_finished ?  'checked':''} 
                                        />             
                    </div>`             

                }
                $('#card-container').html(text);

            } ,
            error: function(data){
                console.log('Error Detected');
            }
        })}

    function submitForm(){
            $.ajax({
                type: "POST",
                url: "{% url 'todolist:create_task_ajax' %}",
                data: {
                    title: $("#inputTitle").val(),
                    description: $("#inputDescription").val(),
                    csrfmiddlewaretoken: "{{ csrf_token }}",
                  },
                dataType: "json",
                success: function(){
                    $("#modalForm").modal('hide')
                    makeCards()
                },
                error: function(error){
                    alert("error")
                }
            })
            return false;
        
    }
```



