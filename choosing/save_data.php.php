<?php
// Replace these values with your own MySQL server settings
$host = "DESKTOP-CIVFILD";
$username = "senioretai@gmail.com";
$password = "GSok%f`puiAF~4n%8hnXmh=fB";
$dbname = "landing_page_data";

// Connect to the MySQL server
$conn = new mysqli($host, $username, $password, $dbname);

// Check for errors
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Prepare and execute the INSERT statement
$stmt = $conn->prepare("INSERT INTO form_data (list1, list2, list3, list4) VALUES (?, ?, ?, ?)");
$stmt->bind_param("ssss", $_POST['list1'], $_POST['list2'], $_POST['list3'], $_POST['list4']);
$stmt->execute();

// Close the database connection
$stmt->close();
$conn->close();

// Redirect back to the form page
header("Location: index.html");
exit();
?>
