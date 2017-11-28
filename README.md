# Panorama_Valhalla

1. Install valhalla via: https://github.com/valhalla/valhalla

2. Make sure to install the Kentucky tileset via: http://download.geofabrik.de/north-america/us/kentucky-latest.osm.pbf

3. Replace all available Valhalla source code files with the equivalent Panorama-Valhalla repo files

4. Follow instructions at https://github.com/valhalla/valhalla for initial compile

5. After initial compile, this abreviated compile process can be used:
	make clean
	./autogen.sh
	./configure
	make test -j$(nproc)
	sudo make install

6. To run the code, in the highest level Valhalla directory execute the following:
	valhalla_route_service valhalla.json 1

7. In a secondary terminal execute:
	curl http://localhost:8002/route --data '{"locations":[{"lat":38.042126,"lon":-84.555496,"type":"break","city":"Lexington","state":"KY"},{"lat":38.02869,"lon":-84.602348,"type":"break","city":"Lexington","state":"KY"}],"costing":"auto","directions_options":{"units":"miles"}}' | jq '.' > ../results/my_route.json

8. The result of the route should be stored in "my_route.json" located in the results directory.
	a. To see the route on a map do the following:
		I. go to the demos/polyline/ directory
		II. drop index.html onto a web browser
		II. in the "Encoded Line:" box enter "shape" parameter from my_route.json. Ex: "shape":
		"c~{pgArkzg`DhGcG~v@so@hCgDpBuDl@yB^}@z@uDfDiWbFm_@VyBd@yCjL_|@dErFl_@pGhVhCfNl@pXNhf@uErLkBhGyAjKiC`MeEtJgErQmJfNmIxLoJjAgCt@yBd@yBvc@uZbK_IjGeElJeFzP_IzKuD~SsGjsAm_@xGeD|@_@hHuDnHuEbLoIlJoIpGeEzAm@xB?zA?zA\\rFjBzt@b[`Cz@nh@|Tzo@vY|r@rZhl@xWxp@tYlKpG`LpHhHrFrKlJpMxM|c@|h@vb@|i@lK|JvCfCnDjBfDxA~C|@~Cl@tJl@fIm@vDm@xA]hC}@dEiBrFwDjFcF|OsQlFsFzEuE|EuDnHuErFwCjk@c\\nw@ed@|DyB`Dm@dToHtEiC|TmUpRc[zUm_@pQgX|EqG|EuEdEwCbGgErKuD`B]nD_@lOgDrLsEbFiCfIqHdEuDp\\|r@xMvYjFbFfDhC|DhBhHdExChChBvCxB`IlEzJpRn^~CbFfIzL`CbFxB~HpBfNrA|JrArFpBbGrtAxhCzUfc@jxAdkC`|@f`Bx_BnyCrUhb@ln@~eA|OzVhW~]dUdZlT`\\zUr[vXl^b\\ja@rF~H|Tp\\~X~]bUhWnJxL`RlThMdPfHhMjQr[xLzUlKfXnIxWbFdO|IdZrB~H~CxMxLdo@pGva@`Ibf@pGtd@d@fDpL~{@t@dEtEhXtDjVnI~]tE|SlEhMxMp\\`LrPnNnTbLbPzPbQnNhMnOzLhQxLnNxLrQdOpQhNfNtN`MvNzLrQ{LhL_CbG?xB\\hCrAvChCxBrJjKrLlKxGzKpB`GjAtEfDzU|E`]jAlJl@`Hd@bG`CvXhBjVFdYNhMTtOGtEMxBeAfDaBxBmJ~HyHrF_IrFebBfmAgc@p[c`@hXgDfC{AlAML_DfD_@\\oN`Swg@ju@a\\~f@gOfYo]tn@}EnIcFnHs[vYwSpQwSpRs@l@gDtDeKbQuEnIcFnI_ItOyMjVyBdE_DtEuDnHiCrGwC|Iq]flA}DtPoCzJgEjLqGzK_TxWgg@tn@us@z~@_s@|}@aCvC{EnI}E~I_D|IqBzK}E~q@m@xBcAzAcBjBkA\\qB\\cB]_D{AoIqGqnGavEi_BkjAyfDqbCwSiMgOqHe~@{_@geBgw@mZyMag@kUst@s\\ow@o]evB{~@nRbo@xBjLlAxL\\zKLzLk@xVsA|Tu@nI{AlJiB|J_Opp@s[huAuYtmAwHdZcLre@sAnH}@`H]`I]jKGxW{@n|@m@nr@Wha@M~]e@xv@GzKyBz@kB\\mD]aCkAkGsFwCwCiCgDyByB}DiCkFiCuJsFaHqGyGaHqHaHmEuEaCiB"
		so enter in:
		c~{pgArkzg`DhGcG~v@so@hCgDpBuDl@yB^}@z@uDfDiWbFm_@VyBd@yCjL_|@dErFl_@pGhVhCfNl@pXNhf@uErLkBhGyAjKiC`MeEtJgErQmJfNmIxLoJjAgCt@yBd@yBvc@uZbK_IjGeElJeFzP_IzKuD~SsGjsAm_@xGeD|@_@hHuDnHuEbLoIlJoIpGeEzAm@xB?zA?zA\\rFjBzt@b[`Cz@nh@|Tzo@vY|r@rZhl@xWxp@tYlKpG`LpHhHrFrKlJpMxM|c@|h@vb@|i@lK|JvCfCnDjBfDxA~C|@~Cl@tJl@fIm@vDm@xA]hC}@dEiBrFwDjFcF|OsQlFsFzEuE|EuDnHuErFwCjk@c\\nw@ed@|DyB`Dm@dToHtEiC|TmUpRc[zUm_@pQgX|EqG|EuEdEwCbGgErKuD`B]nD_@lOgDrLsEbFiCfIqHdEuDp\\|r@xMvYjFbFfDhC|DhBhHdExChChBvCxB`IlEzJpRn^~CbFfIzL`CbFxB~HpBfNrA|JrArFpBbGrtAxhCzUfc@jxAdkC`|@f`Bx_BnyCrUhb@ln@~eA|OzVhW~]dUdZlT`\\zUr[vXl^b\\ja@rF~H|Tp\\~X~]bUhWnJxL`RlThMdPfHhMjQr[xLzUlKfXnIxWbFdO|IdZrB~H~CxMxLdo@pGva@`Ibf@pGtd@d@fDpL~{@t@dEtEhXtDjVnI~]tE|SlEhMxMp\\`LrPnNnTbLbPzPbQnNhMnOzLhQxLnNxLrQdOpQhNfNtN`MvNzLrQ{LhL_CbG?xB\\hCrAvChCxBrJjKrLlKxGzKpB`GjAtEfDzU|E`]jAlJl@`Hd@bG`CvXhBjVFdYNhMTtOGtEMxBeAfDaBxBmJ~HyHrF_IrFebBfmAgc@p[c`@hXgDfC{AlAML_DfD_@\\oN`Swg@ju@a\\~f@gOfYo]tn@}EnIcFnHs[vYwSpQwSpRs@l@gDtDeKbQuEnIcFnI_ItOyMjVyBdE_DtEuDnHiCrGwC|Iq]flA}DtPoCzJgEjLqGzK_TxWgg@tn@us@z~@_s@|}@aCvC{EnI}E~I_D|IqBzK}E~q@m@xBcAzAcBjBkA\\qB\\cB]_D{AoIqGqnGavEi_BkjAyfDqbCwSiMgOqHe~@{_@geBgw@mZyMag@kUst@s\\ow@o]evB{~@nRbo@xBjLlAxL\\zKLzLk@xVsA|Tu@nI{AlJiB|J_Opp@s[huAuYtmAwHdZcLre@sAnH}@`H]`I]jKGxW{@n|@m@nr@Wha@M~]e@xv@GzKyBz@kB\\mD]aCkAkGsFwCwCiCgDyByB}DiCkFiCuJsFaHqGyGaHqHaHmEuEaCiB

9. When finished running Valhalla, terminate the program in the 1st terminal window.
