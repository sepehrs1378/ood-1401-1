function get_export(type, values, field_names, table_id) {
  // values = JSON.parse(values);
  console.log("type ==> ", type);
  console.log("values ==> ", values);
  let rows = [];
  values.map((value) => {
    let fields = [];
    field_names.map((field) => {
      fields.push(value.fields[field]);
    });
    rows.push(fields);
  });
  if (type == "csv") {
    let csvContent =
      "data:text/csv;charset=utf-8," +
      field_names +
      "\r\n" +
      rows.map((e) => e.join(",")).join("\n");
    var encodedUri = encodeURI(csvContent);
    var link = document.createElement("a");
    link.setAttribute("href", encodedUri);
    link.setAttribute("download", "export.csv");
    document.body.appendChild(link); // Required for FF

    link.click();
  } else if (type == "pdf") {
    const element = document.getElementById(table_id);
    console.log(element);
    html2pdf().from(element).save("export.pdf");
  }
}
