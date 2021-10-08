# exchangeRates_modularPlotter
A script that charts multiple versions of a currency's rate against a flexible number of other currencies, and displays them in a modular grid.

![newplot(18)](https://user-images.githubusercontent.com/69304112/136550107-021272c8-5885-417a-8d94-fa34e651cd24.png)

Each chart is given it's own subplot, and the layout of this grid is optimised through a calculation that:

- produces an x by x grid where the number of currencies to be charted is divisible by x
- produces a slightly wider, though as 'square' as possible, grid where it it not 

The exchange rates are pulled from APIs courtesy of www.frankfurter.app.

A version that randomly selects a base currency and the currencies to compare against is also included. Choose 4-20 currencies, or None and a random number of charts will be created.

![newplot(19)](https://user-images.githubusercontent.com/69304112/136550202-14994ab6-25ca-49bb-ad05-5def6902cd73.png)
