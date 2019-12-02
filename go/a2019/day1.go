package a2019

import (
	"bufio"
	"log"
	"os"
	"strconv"
)

func computeFuel(path string, fuel func(int) int) (int, error) {
	file, err := os.Open(path)
	if err != nil {
		return -1, err
	}
	defer file.Close()

	var total_fuel int = 0
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		i, err := strconv.Atoi(scanner.Text())
		if err != nil {
			return -1, err
		}
		total_fuel += fuel(i)
	}
	return total_fuel, scanner.Err()
}

func simple_fuel(mass int) int {
	return (mass / 3) - 2
}

func complex_fuel(mass int) int {
	fuel := simple_fuel(mass)
	if fuel <= 0 {
		return 0
	}
	return complex_fuel(fuel) + fuel
}

func ComputeDay1(data_path string) {
	log.Println("Compute 2019 day 1:")
	log.Println("Part One...")
	result, err := computeFuel(data_path, simple_fuel)
	if err != nil {
		log.Fatal("Erroro computing")
	}
	if result == 3402609 {
		log.Println("Result right")
	} else {
		log.Fatal("Wrong result expected 3402609 but it was ", result)
	}
	log.Println("Part Two...")
	result, err = computeFuel(data_path, complex_fuel)
	if err != nil {
		log.Fatal("Erroro computing")
	}
	if result == 5101025 {
		log.Println("Result right")
	} else {
		log.Fatal("Wrong result expected 5101025 but it was ", result)
	}
}
