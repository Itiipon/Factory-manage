$(document).ready(function() {
 
  
    // let empDataTable = $('#empTable').DataTable({
    //             "dom": 'Btip',  
    //             'processing': true,
    //             'serverSide': true,
    //             'serverMethod': 'post',
    //             'ajax': {
    //                 'url':'/api/employee'
    //             },
    //             "pageLength": 10,
    //             'lengthMenu': false,
    //         });
    //         $('#search').keyup(function () {
    //             empDataTable.search($(this).val()).draw();
    //         });

    let empDataTable = $('#empTable').DataTable({
        "dom": 'Btip',
        "processing": true,
        "pageLength": 10,
        // "scrollY": 300,
        // "scrollX": true,
        // "order": [[ 0, "desc" ]],
        "oLanguage": {
          "sLengthMenu": "แสดง _MENU_ ลำดับ ต่อหน้า",
          "sZeroRecords": "ไม่พบข้อมูลที่ค้นหา",
          "sInfo": "แสดง _START_ ถึง _END_ ของ _TOTAL_ ลำดับ",
          "sInfoEmpty": "แสดง 0 ถึง 0 ของ 0 ลำดับ",
          "sInfoFiltered": "(แสดงค้นหาทั้งหมด _MAX_ รายการ)",
          "oPaginate": {
            "sFirst": "หน้าแรก",
            "sLast": "หน้าสุดท้าย",
            "sNext": "ถัดไป",
            "sPrevious": "ก่อนหน้า"
          }
        }
      });
      oTable = $('#empTable').DataTable();
      oTable.buttons('.buttons-csv').nodes().css("display", "none");
      oTable.buttons('.buttons-excel').nodes().css("display", "none");
      oTable.buttons('.buttons-print').nodes().css("display", "none");
      oTable.buttons('.buttons-pdf').nodes().css("display", "none");
      oTable.buttons('.buttons-copy').nodes().css("display", "none");
      $('#search').keyup(function () {
        oTable.search($(this).val()).draw();
      });
      $('#toexcel').on('click', function () {
        oTable.button('.buttons-excel').trigger();
      })
 
});


