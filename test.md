<!DOCTYPE HTML>
<html>
<head>
<meta charset="UTF-8" />
<title>Javascript+HTML用正则表达式写一段输入的验证代码</title>
<style type="text/css">
table {
    position: relative;
    margin: auto;
    font-family: Consolas;
    font-size: 12px;
    border: 1px solid black;
    border-collapse: collapse;
    width: 800px;
}
 
table tr td {
    border: 1px solid black;
}
 
.center {
    text-align: center;
}
</style>
<script type="text/javascript">
    var V = {
        date: new Date,
        isError: true,
        validationType: [
                           'cannot be blank',
                            'must be a valid email',
                            'must contain only numbers,single spaces.',
                            'must contain between 13 & 18 numbers, and single spaces.',
                            'expiry date cannot be expired.'
                         ],
        trim: function(v)
        {
            return v.replace(/^\s*|\s*$/g, '');
        }, 
        validateOnblur: function(obj, validationType)
        {
            var val = V.trim(obj.value);
            switch (validationType)
            {
                case 0:
                    if (V.trim(obj.value) == '')
                    {
                        obj.value = '';
                        return V.validationType[0];
                    }
                    return '';
                case 1:
                    if (!/^[\w\-]+@[\w\-]+\.\w+$/.test(val))
                    {
                        obj.value = '';
                        return V.validationType[1];
                    }
                    return '';
                case 2:
                    if (!/^(\+\(\d+\))?\d+$/.test(val))
                    {
                        obj.value = '';
                        return V.validationType[2];
                    }
                    return '';
                case 3:
                    if (!/^[\d\s]{13,18}$/.test(val))
                    {
                        obj.value = '';
                        return V.validationType[3];
                    }
                    return '';
                case 4:
                    var expirydate = document.getElementsByName('expirydate');
                    var year = expirydate[0].value;
                    var month = expirydate[1].value;
                    if (new Date(year, parseInt(month) - 1, 0) <= V.date)
                    {
                        return V.validationType[4];
                    }
                    return '';
                default:
                    return '';
            }
        },
        checkNow: function(obj)
        {
            var _name = obj.name, validationType = -1;
            if (_name == 'firstname' || _name == 'lastname' || _name == 'address')
            {
                validationType = 0;
            }
            else if (_name == 'email')
            {
                validationType = 1;
            }
            else if (_name == 'phone')
            {
                validationType = 2;
            }
            else if (_name == 'credit')
            {
                validationType = 3;
            }
            else if (_name == 'expirydate')
            {
                validationType = 4;
            }
            var cell = obj.parentElement;
            if (cell.children[cell.children.length - 1].tagName.toLowerCase() == 'div')
            {
                cell.removeChild(cell.children[cell.children.length - 1]);
                V.isError = false;
            }
            var error = V.validateOnblur(obj, validationType);
            if (error != '')
            {
                var info = document.createElement('div');
                info.style.color = 'red';
                info.innerText = error;
                cell.appendChild(info);
                V.isError = true;
            }
        },
        displayError: function(rows, len, flag)
        {
            for ( var i = 0; i < len; i++)
            {
                var cell = rows[i].cells[1];
                if (!cell)
                {
                    continue;
                }
                var obj = cell.children[0];
                if (flag)
                {
                    if (typeof obj.value != 'undefined')
                    {
                        V.checkNow(obj);
                    }
                }
                else
                {
                    obj.onblur = function()
                    {
                        V.checkNow(this);
                    }
                    if (obj.tagName.toLowerCase() == 'select')
                    {
                        cell.children[1].onblur = function()
                        {
                            V.checkNow(this);
                        }
                    }
                }
            }
        }
    };
    window.onload = function ()
    {
        var form = document.formValidation;
        var table = form.getElementsByTagName('table')[0];
        var rows = table.rows, len = rows.length;
        document.getElementById('submit').onclick = function()
        {
            V.displayError(rows, len, true);
        }
         
        form.onsubmit = function()
        {
            return !V.isError;
        }
        V.displayError(rows, len, false);
         
        var date = V.date;
        var expirydate = document.getElementsByName('expirydate');
        for ( var i = 2014; i < 2055; i++)
        {
            var option = document.createElement('option');
            option.value = i;
            option.innerText = i;
            expirydate[0].appendChild(option);
        }
        expirydate[0].value = date.getFullYear();
    }
</script>
</head>
<body>
    <form name="formValidation" method="post" action="">
        <table>
            <caption>!Form Validation!</caption>
            <tr>
                <td>first name:</td>
                <td><input type="text" name="firstname" /></td>
            </tr>
            <tr>
                <td>last name:</td>
                <td><input type="text" name="lastname" /></td>
            </tr>
            <tr>
                <td>address:</td>
                <td><textarea name="address"></textarea></td>
            </tr>
            <tr>
                <td>email:</td>
                <td><input type="text" name="email" /></td>
            </tr>
            <tr>
                <td>phone:</td>
                <td><input type="text" name="phone" /></td>
            </tr>
            <tr>
                <td>delivery method:</td>
                <td>
                    <label><input type="radio" name="delivery" checked="checked" />regular post</label>
                    <label><input type="radio" name="delivery" />courier</label>
                    <label><input type="radio" name="delivery" />express courier</label>
                </td>
            </tr>
            <tr>
                <td>credit card number field: </td>
                <td><input type="text" name="credit" /></td>
            </tr>
            <tr>
                <td>expiry date:</td>
                <td>
                    <select name="expirydate"></select> year
                    <select name="expirydate">
                    <option value="1">01</option>
                    <option value="2">02</option>
                    <option value="3">03</option>
                    <option value="4">04</option>
                    <option value="5">05</option>
                    <option value="6">06</option>
                    <option value="7">07</option>
                    <option value="8">08</option>
                    <option value="9">09</option>
                    <option value="10">10</option>
                    <option value="11">11</option>
                    <option value="12">12</option>
                    </select> month
                </td>
            </tr>
            <tr>
                <td class="center" colspan="2">
                    <label><input type="checkbox" name="newletter" />please sign me up for the newletter</label>
                </td>
            </tr>
            <tr>
                <td class="center" colspan="2">
                    <input type="submit" value="submit" id="submit" /><input type="reset" value="reset" id="reset" />
                </td>
        </table>
    </form>
</body>
</html>
