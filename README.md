# data-preprocessing
Data Pre-Processing tools like annotation, metadata extraction, etc. for various data, including image files, audio, and video files. 
<hr>
<h2>Image_annotation</h2>
<hr>
<p>This program aims to recognize objects in any given picture and draw bounding boxes around the object.<br>The objective lies in identifying the objects for further data pre-processing !</p>
<br>
<h2>For Windows</h2>
<h3>Step 1:</h3>
<h5>Install the respective dependencies: </h5>
<ul>
  <li>yolov3.weights</li>
  <li>yolov3.cfg</li>
  <li>coco.names</li>
</ul>
<p>You may visit the official website of YOLO to get the dependencies, the command prompt commands are as follows for the respective dependencies: </p>
<ol>
  <li>for yolov3.weights<br><pre>wget https://pjreddie.com/media/files/yolov3.weights</pre></li>
  <li>for yolov3.cfg<br><pre>wget https://github.com/pjreddie/darknet/blob/master/cfg/yolov3.cfg?raw=true -O yolov3.cfg</pre></li>
  <li>for coco.names<br><pre>wget https://github.com/pjreddie/darknet/blob/master/data/coco.names?raw=true -O coco.names</pre></li>
</ol>

<h2>For Mac</h2>
<h5>You may visit the official YOLO website to install the dependencies or use these terminal commands: </h5>
<ol>
  <li>for yolov3.weights<br><pre>curl -O https://pjreddie.com/media/files/yolov3.weights</pre></li>
  <li>for yolov3.cfg<br><pre>curl -o yolov3.cfg https://raw.githubusercontent.com/pjreddie/darknet/master/cfg/yolov3.cfg</pre></li>
  <li>for coco.names<br><pre>curl -o coco.names https://raw.githubusercontent.com/pjreddie/darknet/master/data/coco.names</pre></li>
</ol>

<h3>Step 2:</h3>
<h5>Place the Files:</h5>
<p>Ensure these files are in the same directory as your Python script. The directory should look like this:</p>
<pre>your_project_directory/
├── yolov3.weights
├── yolov3.cfg
├── coco.names
└── your_script.py
</pre>

<h3>Step 3:</h3>
<p>Add an image in the same directory as the main.py file and run the script</p>
<em>Note:</em> for Mac users, there might occur a warning after successfully running the programming explaining the warning is related to macOS's security features and how macOS applications handle restorable state (like remembering window positions, open documents, etc.) when they are relaunched.
<br>
The warning may look like this: 
<pre>WARNING: Secure coding is not enabled for restorable state! Enable secure coding by implementing NSApplicationDelegate.applicationSupportsSecureRestorableState: and returning YES.</pre>
