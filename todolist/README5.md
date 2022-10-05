# **PBP Assignment 5**

Nama : Carlene Annabel

NPM : 2106752211

Kelas :D

##  **Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?** 

Inline CSS merupakan penulisan CSS yang dilakukan didalam tag elemen yang akan di styling , Internal CSS merupakan cara penulisan CSS yang dilakukan pada file yang sama dengan file HTML. Sedangkan External CSS adalah cara penulisan CSS pada file yang terpisah dari HTML.

Keuntungan dari Inline CSS adalah kita dapat memasukan dengan mudah dan cepat aturan - aturan CSS pada halaman HTML.Kekurangan, memakan waktu lebih banyak karena memasukan CSS styling pada setiap tag elemen.

Keuntungan dari Internal CSS adalah kita dapat menggunakan class dan id selector seperti

```js
    .class {
    property1 : value1; 
    property2 : value2; 
    property3 : value3; 
    }
```

Kerugiannya adalah saat memasukkan kode ke dokumen HTML dapat meningkatkan ukuran halaman dan waktu loading.

Keuntungan dari External CSS, karena kode CSS berada pada halaman yang berbeda, kode HTML yang kita miliki akan memiliki struktur yang lebih rapih dann ukuran yang lebih sedikit. Kerugiannya adalah, halaman yang kita miliki mungkin tidak akan dirender dengan benar sampai exteral CSS nya selesai di load.

##  ** Jelaskan tag HTML5 yang kamu ketahui.** 

1. <a> , mendefinisikan hyperlink
2. <area>, mendefinisikan area spesifik di dalam image map
3. <div> menspesifikasikan division atau sebuah section dalam dokumen
4. <input> mendefinisikan kontrol input
5. <img> merepresentasikan gambar

## **Jelaskan tipe-tipe CSS selector yang kamu ketahui.**

1. element , cth: p , selects semua elemen <p>
2. #id , cth: #lastname, selects semua elemen dengan id="lastname"
3. :visited, cth: a:visited, selects semua link yang sudah di visit

## **Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.**

1. Mencari design template yang menarik untuk dijadikan referensi
2. Kustomisasi templat untuk halaman login, register, create-task, dan todolist dengan CSS framework bootstrap.
3. Membuat cards pada halaman todolist dengan kode berikut

```js
<div class="container d-flex flex-wrap flex-row ">
                {% for task in todolist %}
                <div class="m-2 card p-2">
                    <p class="text font-weight-bold">Task : {{task.title}}</p>
                    <p>Description : {{task.description}}</p>
                    <p>Created : {{task.date}}</p>
                    <p>Status : 
                        {% if task.is_finished == True %}
                            <span class= "Completed text-success">Completed</span>
                        {% else %}
                            <span class="unfinished text-danger">Unfinished</span>
                        {% endif %}
                    </p>
                    <button class="btn" ><a href="{% url 'todolist:delete' task.id %}"><i class="fa fa-trash"></i></a></button>
                    <input class='todolist-check' 
                                    type="checkbox" 
                                    id='{{task.id}}' 
                                    value= '{{task.ud}'
                                    name="finishbtn"
                                    {% if task.is_finished %} checked {% endif %}
                                    onchange="location.href='{% url 'todolist:mark_as_finished' task.id %}'" />             
                </div>
</div>
```

4. Membuat keempat halaman tersebut menjadi responsive dengan bootstrap. Seperti menambahkan hover, overflow, mengubah display menjadi flex , dll.

