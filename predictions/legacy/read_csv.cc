#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>
#include <cmath>

struct Coordinate
{
	float lng;
	float lat;
	int score;

	Coordinate():lng(1.0), lat(1.0), score(1) {}
};

bool float_approx_equals(float a, float b, float epsilon);

bool float_approx_equals(float a, float b, float epsilon = 0.000001)
{
	std::cout << "stuff" << std::endl;
	return std::abs(a - b) < epsilon;
}

void log_csv(float lat, float lng)
{
	std::ofstream storage_csv;
	storage_csv.open("route_log.csv", std::ofstream::app);
	storage_csv << lat << "," << lng << std::endl;
	storage_csv.close();
}


int main()
{
	std::string filename = "parkers_mill.csv";
	std::string current_line = "";

	std::vector<Coordinate> graded_edges;

	std::ifstream myfile(filename.c_str());

	if(myfile)
	{
		int cnt = 0;
		while(getline(myfile, current_line))
		{
			if(cnt > 0)
			{
				std::stringstream linestream(current_line);
				std::string value;

				Coordinate tmp_coordinate;

				getline(linestream, value, ',');
				tmp_coordinate.lat = std::stod(value);
				getline(linestream, value, ',');
				tmp_coordinate.lng = std::stod(value);
				getline(linestream, value, ',');
				tmp_coordinate.score = std::stoi(value);
				graded_edges.push_back(tmp_coordinate);		
			}
			cnt++;
		}
	}

	myfile.close();

	std::cout.precision(17);

	/*
	for(int i = 0; i < graded_edges.size(); i++)
	{
		std::cout <<"Lat: " << std::fixed << graded_edges[i].lat << " Lng: " << std::fixed <<  graded_edges[i].lng << " Score: " << graded_edges[i].score << std::endl;
	}

	if(float_equals(graded_edges[0].lat, -84.555718))
	{
		std::cout << "equal " << std::abs(graded_edges[0].lat - -84.555718) << std::endl;
	}
	else
	{
		std::cout << "not equal" << std::abs(graded_edges[0].lat - -84.555718) << std::endl;
	}
	*/

	for(int i = 0; i < graded_edges.size(); i++)
	{
		if(float_approx_equals(graded_edges[i].lat, -84.557045, 0.00001) && float_approx_equals(graded_edges[i].lng, 38.042949, 0.00001))
			std::cout <<"Lat: " << std::fixed << graded_edges[i].lat << " Lng: " << std::fixed <<  graded_edges[i].lng << " Score: " << graded_edges[i].score << std::endl;
		else
			std::cout << "not" << std::endl;
	}


	std::ofstream storage_csv;
	storage_csv.open("route_log.csv", std::ofstream::app);
	storage_csv << "latitude" << "," << "longitude" << std::endl;
	storage_csv.close();

	float some_val = -84.557045;
	float some_val2 = 38.042949;

	log_csv(some_val, some_val2);
	log_csv(-125.543, 0.1);
	log_csv(24.87866, 38.0429498754);

	return 0;
}


