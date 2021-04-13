(feature-note)=

# Voting for new features

You can help us to prioritise development of new features by leaving a [👍 reaction](https://github.blog/2016-03-10-add-reactions-to-pull-requests-issues-and-comments/) on the first comment of any `enhancement` issue.

Below is a list of all current enhancement issues from our core repositories,[^a] ordered by 👍
Click the `+` to see more details.

[^a]: The data in this table is updated every hour.

<div class="full-width">

```{include} issue-votes.txt
```

</div>

<!-- DataTables to make the table above look nice -->
<link rel="stylesheet"
    href="https://cdn.datatables.net/1.10.24/css/jquery.dataTables.min.css">
<script type="text/javascript" src="https://cdn.datatables.net/1.10.24/js/jquery.dataTables.min.js"></script>

<script>
$(document).ready( function () {
    $('table').DataTable( {
        "order": [[ 0, "desc" ]]
    });
} );
</script>
