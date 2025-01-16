from dashboard import AgriculturalDashboard
from map_visualization import AgriculturalMap
import streamlit as st
from streamlit_folium import folium_static  # To display Folium maps in Streamlit

class IntegratedDashboard:
    def __init__(self, data_manager):
        """
        Initialize the Integrated Dashboard.
        Combines Bokeh and Folium visualizations.
        """
        self.data_manager = data_manager
        self.bokeh_dashboard = AgriculturalDashboard(data_manager)
        self.map_view = AgriculturalMap(data_manager)

    def initialize_visualizations(self):
        """
        Initialize all visual components (Bokeh and Folium).
        """
        try:
            # Initialize Bokeh layout
            self.bokeh_layout = self.bokeh_dashboard.create_layout()

            # Initialize Folium map
            self.map_view.create_base_map()
            self.map_view.add_yield_history_layer()
            self.map_view.add_risk_heatmap()

            print("Visualizations initialized successfully.")
        except Exception as e:
            print(f"Error initializing visualizations: {e}")

    def create_streamlit_dashboard(self):
        """
        Create a Streamlit interface integrating all visualizations.
        """
        try:
            # Custom CSS
            st.markdown("""
            <style>
                /* Example: Change the background color of the entire page */
                body {
                    background-color: #f0f2f6;
                }

                /* Example: Change the title color */
                h1 {
                    color: #4CAF50;
                }

                /* Example: Change the header color */
                h2 {
                    color: #FF5722;
                }

                /* Example: Adjust the padding of the Streamlit container */
                .stApp {
                    padding: 2rem;
                }

                /* Example: Style the warning message */
                .stWarning {
                    background-color: #FFF3CD;
                    color: #856404;
                    border-radius: 5px;
                    padding: 10px;
                }

                /* Example: Style the error message */
                .stError {
                    background-color: #F8D7DA;
                    color: #721C24;
                    border-radius: 5px;
                    padding: 10px;
                }

                /* Example: Style the Bokeh chart container */
                .stBokehChart {
                    border: 1px solid #ddd;
                    border-radius: 5px;
                    padding: 10px;
                }
            </style>
            """, unsafe_allow_html=True)

            st.title("Tableau de Bord Agricole Intégré")

            # Initialize visualizations
            self.initialize_visualizations()

            # Display Bokeh visualizations
            st.header("Visualisations Bokeh")
            if self.bokeh_layout:
                st.bokeh_chart(self.bokeh_layout, use_container_width=True)
            else:
                st.warning("Bokeh layout could not be generated.")

            # Display Folium map
            st.header("Carte Interactive (Folium)")
            if self.map_view.map:
                map_file = "integrated_map.html"
                self.map_view.map.save(map_file)
                st.markdown(
                    f'<iframe class="folium-map" src="{map_file}" width="100%" height="600px"></iframe>',
                    unsafe_allow_html=True,
                )
            else:
                st.warning("Folium map could not be generated.")

        except Exception as e:
            st.error(f"Error creating Streamlit dashboard: {e}")
            print(f"Error creating Streamlit dashboard: {e}")

    def update_visualizations(self, parcelle_id):
        """
        Update all visualizations for a given parcel.
        """
        try:
            # Update Bokeh plots
            self.bokeh_dashboard.create_data_sources()

            # Update Folium map
            self.map_view.create_base_map()
            self.map_view.add_yield_history_layer()
            self.map_view.add_risk_heatmap()

            print(f"Visualizations updated for parcelle_id: {parcelle_id}")
        except Exception as e:
            print(f"Error updating visualizations: {e}")

from data_manager import AgriculturalDataManager

if __name__ == "__main__":

    # Load data
    data_manager = AgriculturalDataManager()
    data_manager.load_data()

    # Initialize dashboard
    dashboard = IntegratedDashboard(data_manager)

    # Create Streamlit interface
    dashboard.create_streamlit_dashboard()
