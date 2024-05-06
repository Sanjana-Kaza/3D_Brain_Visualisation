import streamlit as st
import subprocess

def launch_fsleyes(file_paths, color_maps):
    command = ["fsleyes"]
    for file_path, color_map in zip(file_paths, color_maps):
        command.extend([file_path, "-cm", color_map])

    # Execute the command and capture the output and errors
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode != 0:
        st.error(f"Error launching FSLeyes: {result.stderr}")
    else:
        st.success("FSLeyes launched successfully!")

def display_tumor_details():
    st.markdown("## Spatial Tumor Depth Analysis ##")
    st.markdown("###### W.R.T Topmost Tumor Point #####")
    st.text('Tumor depth from topmost brain voxel_z   (in voxel units): 77\n'
            'Tumor depth from topmost brain voxel_z   (in mm): 77.0\n'
            'Tumor depth from bottomost brain voxel_z (in voxel units): -77\n'
            'Tumor depth from bottomost brain voxel_z (in mm): -77.0')
    st.markdown('___________________________________________________________')
    
    st.markdown("###### W.R.T Rightmost Tumor Point #####")
    st.text('Tumor depth from rightmost brain voxel_x (in voxel units): 108\n'
            'Tumor depth from rightmost brain voxel_x (in mm): 108.0\n'
            'Tumor depth from leftmost brain voxel_x  (in voxel units): -131\n'
            'Tumor depth from leftmost brain voxel_x  (in mm): -131.0')
    st.markdown('___________________________________________________________')

    st.markdown("###### W.R.T Backmost Tumor Point #####")
    st.text('Tumor depth from backmost brain voxel_y (in voxel units): 83\n'
            'Tumor depth from backmost brain voxel_y (in mm): 83.0\n'
            'Tumor depth from frontmost brain voxel_y (in voxel units): -156\n'
            'Tumor depth from frontmost brain voxel_y (in mm): -156.0')

def display_brain_regions():
    regions = [
        'Left Cerebral Cortex:0.0013',
        'Brain-Stem:0.6528',
        'Right Cerebral White Matter:5.5427',
        'Right Cerebral Cortex:15.7124',
        'Right Lateral Ventricle:0.0028',
        'Right Hippocampus:0.0090'
    ]
    st.markdown("## Tumor Distribution Across Brain Regions ##")
    for region in regions:
        st.text(region)

def main():
    st.title("Patient Data Interface")

    # Patient ID input
    patient_id = st.text_input("Enter Patient ID:")
    
    # Button to check ID
    if st.button("Check Patient ID"):
        if patient_id == "3":
            st.session_state.patient_id_15 = True
            st.markdown("# Step 1")
            st.write("<span style='color:red'>Presence of MGMT Promoter not detected!</span>", unsafe_allow_html=True)
            st.write("Due to the absence of the promoter, surgical intervention is recommended. Providing you with 3D Visualisations and Tumor Analysis to facilitate better surgical planning ")
            st.markdown("# Step 2")
            st.write("Generating 3D Tumor Mask for the Tumor Core...")
            st.image('/Users/kaza/Downloads/MLH_Streamlit.jpeg', caption='Image caption')
            st.markdown("# Step 3")
            display_tumor_details()  # Display tumor details right after ID check
            display_brain_regions()  # Display brain region details
        else:
            st.session_state.patient_id_15 = False
            st.write("<span style='color:green'>Presence of MGMT Promoter detected! Chemotherapy is recommended</span>", unsafe_allow_html=True)

    # File inputs and FSLeyes launching logic
    if st.session_state.get('patient_id_15', False):
        st.markdown("## Start FSLeyes for Detailed Image Analysis ##")
        file_path1 = st.text_input("Enter path for file 1:", value="MNI152_T1_1mm_brain.nii.gz")
        file_path2 = st.text_input("Enter path for file 2:", value="registered_brain_03_volume.nii.gz")
        color_map1 = st.text_input("Enter color map for file 1:", value="greyscale")
        color_map2 = st.text_input("Enter color map for file 2:", value="hot")

        if st.button("Launch FSLeyes"):
            file_paths = [file_path1, file_path2]
            color_maps = [color_map1, color_map2]
            st.write("Launching FSLeyes...")
            launch_fsleyes(file_paths, color_maps)

    st.write("Ensure this is run in an environment where FSLeyes is installed.")

if __name__ == "__main__":
    main()
