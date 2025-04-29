export const TABLE_DATA = [
  { rowField1: "Test", rowField2: "Test", rowField3: "Test" },
  { rowField1: "Test", rowField2: "Test", rowField3: "Test" },
  { rowField1: "Test", rowField2: "Test", rowField3: "Test" },
];

export const TABLE_COLUMNS = [
  {
    headerName: "Col title",
    field: "rowField1",
    sortable: true,
    sort: "desc",
    unSortIcon: true,
  },
  { headerName: "Col title", field: "rowField2", sortable: true, unSortIcon: true },
  { headerName: "Col title", field: "rowField3" },
];


export const STATUS_TYPES = [
    {
      id: "1",
      icon: "c-check-16",
      label: "Active",
      isSelected: true
    },
    {
      id: "2",
      icon: "flag16",
      label: "Active & Preferred",
      isSelected: true
    },
    {
      id: "3",
      icon: "cwarning16",
      label: "Not for New Design",
      isSelected: false
    },
    {
      id: "4",
      icon: "ban16",
      label: "Discontinued",
      isSelected: false
    }
  ]