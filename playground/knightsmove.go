package playground

import (
	"fmt"
	"log"
)

func knightsMove() {
	var n, m int
	if _, err := fmt.Scan(&n); err != nil {
		log.Fatal(err)
	}
	if _, err := fmt.Scan(&m); err != nil {
		log.Fatal(err)
	}

	counter := 0
	recurrent(1, 1, n, m, &counter)
	fmt.Println(counter)
}

func recurrent(x, y, fin_x, fin_y int, counter *int) {
	if x == fin_x && y == fin_y {
		*counter++
		return
	}

	if x > fin_x || y > fin_y {
		return
	}

	recurrent(x+1, y+2, fin_x, fin_y, counter)
	recurrent(x+2, y+1, fin_x, fin_y, counter)
	recurrent(x+2, y-1, fin_x, fin_y, counter)
	recurrent(x-1, y+2, fin_x, fin_y, counter)
}
